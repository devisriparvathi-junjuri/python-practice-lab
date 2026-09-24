"""Tests for string and collection practice functions."""

import importlib.util
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).parents[1] / "04_functions" / "practice_functions.py"
spec = importlib.util.spec_from_file_location("practice_functions", MODULE_PATH)
assert spec and spec.loader
practice_functions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(practice_functions)


def test_normalize_words() -> None:
    assert practice_functions.normalize_words([" Python ", "", "DATA"]) == ["python", "data"]


def test_transform_values() -> None:
    assert practice_functions.transform_values([1, 2, 3], lambda value: value * 2) == [2, 4, 6]


@pytest.mark.parametrize("value", ["missing-at", "name@domain", "@example.com"])
def test_email_validation_rejects_invalid_values(value: str) -> None:
    assert not practice_functions.is_valid_email(value)


def test_email_validation_accepts_email_like_value() -> None:
    assert practice_functions.is_valid_email("student@example.com")
