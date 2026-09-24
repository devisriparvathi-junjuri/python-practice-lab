"""Tests for reusable calculator functions."""

import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "04_functions" / "practice_functions.py"
spec = importlib.util.spec_from_file_location("practice_functions", MODULE_PATH)
assert spec and spec.loader
practice_functions = importlib.util.module_from_spec(spec)
spec.loader.exec_module(practice_functions)


def test_adds_integers_and_floats() -> None:
    assert practice_functions.add(2, 3.5) == 5.5


def test_divide_returns_quotient() -> None:
    assert practice_functions.divide(9, 2) == 4.5


def test_divide_rejects_zero() -> None:
    import pytest

    with pytest.raises(ValueError, match="zero"):
        practice_functions.divide(1, 0)
