"""
Unit tests for the calculator app.
"""

import pytest
from calc import calculate

def test_addition():
    assert calculate('+', 1, 2) == 3

def test_subtraction():
    assert calculate('-', 5, 3) == 2

def test_multiplication():
    assert calculate('*', 4, 5) == 20

def test_division():
    assert calculate('/', 10, 2) == 5

def test_division_by_zero():
    assert calculate('/', 5, 0) == "Error: Division by zero is not allowed."

def test_invalid_operation():
    assert calculate('?', 1, 2) == "Unsupported operation."

def test_invalid_number_input():
    with pytest.raises(ValueError):
        calculate('+', 'a', 2)