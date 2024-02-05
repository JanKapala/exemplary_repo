"""
Tests for calc.py using pytest
"""

import pytest
from calc import calculate

def test_addition():
    assert calculate('+', 1, 2) == 3

def test_subtraction():
    assert calculate('-', 5, 3) == 2

def test_multiplication():
    assert calculate('*', 2, 3) == 6

def test_division():
    assert calculate('/', 6, 2) == 3

def test_division_by_zero():
    assert calculate('/', 5, 0) == "Error: Division by zero is not allowed."

def test_invalid_input():
    assert calculate('+', 'a', 'b') == "Error: Please provide valid numbers as arguments.