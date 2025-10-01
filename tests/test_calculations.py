import pytest
from app.calculation import (
    CalculationFactory,
    AddCalculation,
    SubtractCalculation,
    MultiplyCalculation,
    DivideCalculation,
)

@pytest.mark.parametrize("kind,expected_cls", [
    ("add", AddCalculation),
    ("sub", SubtractCalculation),
    ("mul", MultiplyCalculation),
    ("div", DivideCalculation),
    ("ADD", AddCalculation),  # case-insensitive
])
def test_factory_returns_correct_type(kind, expected_cls):
    calc = CalculationFactory.create(kind, 2, 3)
    assert isinstance(calc, expected_cls)

@pytest.mark.parametrize("kind,a,b,expected", [
    ("add", 2, 3, 5),
    ("sub", 5, 3, 2),
    ("mul", 4, 2.5, 10.0),
    ("div", 9, 3, 3.0),
])
def test_get_result(kind, a, b, expected):
    calc = CalculationFactory.create(kind, a, b)
    assert calc.get_result() == expected

def test_factory_unknown_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create("pow", 2, 3)

@pytest.mark.parametrize("bad_a,bad_b", [
    ("x", 1),
    (1, "y"),
    ("x", "y"),
])
def test_input_validation_rejects_non_numbers(bad_a, bad_b):
    with pytest.raises(TypeError):
        CalculationFactory.create("add", bad_a, bad_b)

def test_divide_by_zero_raises_valueerror():
    with pytest.raises(ValueError):
        CalculationFactory.create("div", 1, 0).get_result()
