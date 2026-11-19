from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .core import AnalysisValidationError, extract_json_object, validate_analysis


def main() -> int:
    parser = argparse.ArgumentParser(prog="question-understanding", description="Validate QuestionAnalysis JSON.")
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate", help="Parse and validate a QuestionAnalysis JSON file")
    validate.add_argument("input", type=Path)
    validate.add_argument("--schema", type=Path, default=None)
    validate.add_argument("--normalized-output", type=Path, default=None,
                          help="Write normalized JSON after successful validation")
    args = parser.parse_args()

    try:
        raw = args.input.read_text(encoding="utf-8")
        analysis = extract_json_object(raw)
        errors = validate_analysis(analysis, args.schema)
        if errors:
            print("INVALID QuestionAnalysis:", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            return 2
        if args.normalized_output:
            args.normalized_output.parent.mkdir(parents=True, exist_ok=True)
            args.normalized_output.write_text(
                json.dumps(analysis, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
        print(f"VALID QuestionAnalysis: {analysis['question_id']} ({analysis['status']})")
        return 0
    except (OSError, AnalysisValidationError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
