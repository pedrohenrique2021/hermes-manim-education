import json

import pytest

from hermes_education.question_understanding import (
    AnalysisValidationError,
    build_analysis_prompt,
    extract_json_object,
    validate_analysis,
)


def valid_analysis():
    return {
        "schema_version": "1.0",
        "question_id": "test-math-001",
        "subject": "mathematics",
        "topic": "Algebra",
        "subtopic": "Equação do segundo grau",
        "question_type": "open_ended",
        "statement": "Determine as raízes de x² - 5x + 6 = 0.",
        "objective": "Determinar os valores de x que satisfazem a equação.",
        "given_data": [{"name": "equation", "value": "x^2 - 5x + 6 = 0", "unit": None,
                        "source_evidence": "Equação apresentada no enunciado."}],
        "unknowns": [{"name": "x", "description": "Raízes da equação.", "unit": None}],
        "constraints_and_assumptions": [],
        "visual_inputs": [],
        "key_concepts": ["equação quadrática", "fatoração"],
        "irrelevant_or_contextual_information": [],
        "ambiguities": [],
        "confidence": 0.98,
        "status": "ready_for_solution",
    }


def test_valid_analysis_passes_schema():
    assert validate_analysis(valid_analysis()) == []


def test_missing_required_field_is_rejected():
    payload = valid_analysis()
    del payload["objective"]
    assert any("objective" in error for error in validate_analysis(payload))


def test_invalid_subject_is_rejected():
    payload = valid_analysis()
    payload["subject"] = "chemistry"
    assert validate_analysis(payload)


def test_extract_json_from_fence():
    payload = valid_analysis()
    raw = "```json\n" + json.dumps(payload) + "\n```"
    assert extract_json_object(raw) == payload


def test_multiple_objects_are_rejected():
    with pytest.raises(AnalysisValidationError):
        extract_json_object('{"a": 1} and {"b": 2}')


def test_prompt_keeps_source_question_verbatim():
    prompt = build_analysis_prompt("Enunciado original.", question_id="q-1")
    assert "Enunciado original." in prompt
    assert '"question_id": "q-1"' in prompt
