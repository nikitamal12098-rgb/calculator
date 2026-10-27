import pytest
from calculator import add_numbers


def test_add_positive():
    assert add_numbers(2, 3) == 5


def test_add_negative():
    assert add_numbers(-1, -4) == -5


def test_add_float():
    assert add_numbers(0.5, 0.25) == 0.75

def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)