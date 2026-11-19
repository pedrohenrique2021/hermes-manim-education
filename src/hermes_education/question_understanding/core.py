from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_SCHEMA_PATH = PROJECT_ROOT / "schemas" / "question-analysis.schema.json"


class AnalysisValidationError(ValueError):
    """Raised when a QuestionAnalysis artifact does not satisfy its contract."""


def load_schema(schema_path: str | Path | None = None) -> dict[str, Any]:
    path = Path(schema_path) if schema_path else DEFAULT_SCHEMA_PATH
    try:
        schema = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise AnalysisValidationError(f"Could not load JSON Schema at {path}: {exc}") from exc
    Draft202012Validator.check_schema(schema)
    return schema


def extract_json_object(raw: str) -> dict[str, Any]:
    """Parse a JSON object, accepting a single optional Markdown code fence."""
    text = raw.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()

    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        # Be tolerant of a short preamble, but never silently choose among objects.
        decoder = json.JSONDecoder()
        candidates: list[Any] = []
        for index, char in enumerate(text):
            if char == "{":
                try:
                    candidate, _ = decoder.raw_decode(text[index:])
                except json.JSONDecodeError:
                    continue
                if isinstance(candidate, dict):
                    candidates.append(candidate)
        if len(candidates) != 1:
            raise AnalysisValidationError(
                "Model output must contain exactly one valid JSON object and no competing objects."
            )
        value = candidates[0]

    if not isinstance(value, dict):
        raise AnalysisValidationError("QuestionAnalysis must be a JSON object.")
    return value


def validate_analysis(
    analysis: dict[str, Any], schema_path: str | Path | None = None
) -> list[str]:
    """Return human-readable schema errors; an empty list means valid."""
    validator = Draft202012Validator(load_schema(schema_path))
    errors = sorted(validator.iter_errors(analysis), key=lambda e: list(map(str, e.absolute_path)))
    return [
        f"{'.'.join(map(str, error.absolute_path)) or '$'}: {error.message}"
        for error in errors
    ]


def build_analysis_prompt(
    statement: str,
    *,
    question_id: str,
    source: dict[str, Any] | None = None,
    visual_inputs: list[dict[str, Any]] | None = None,
) -> str:
    """Build the task prompt consumed by the active Hermes Agent model."""
    if not statement or not statement.strip():
        raise ValueError("statement must not be empty")
    context = {
        "question_id": question_id,
        "statement": statement.strip(),
        "source": source,
        "visual_inputs": visual_inputs or [],
    }
    return (
        "Analyze the following vestibular question according to the Question Understanding "
        "contract. Return exactly one JSON object, with no Markdown fence or commentary.\n\n"
        "INPUT:\n" + json.dumps(context, ensure_ascii=False, indent=2) + "\n\n"
        "The JSON Schema is schemas/question-analysis.schema.json. Do not solve the question; "
        "identify what is given, what is asked, constraints, concepts, ambiguity and readiness."
    )
