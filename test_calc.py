"""
Unit tests for calc.py
"""

import unittest
from calc import calculate

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate('+', 1, 2), 3)

    def test_subtraction(self):
        self.assertEqual(calculate('-', 5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(calculate('*', 2, 3), 6)

    def test_division(self):
        self.assertEqual(calculate('/', 6, 2), 3)

    def test_division_by_zero(self):
        self.assertEqual(calculate('/', 5, 0), "Error: Division by zero is not allowed.")

    def test_invalid_input(self):
        self.assertEqual(calculate('+', 'a', 'b'), "Error: Please provide valid numbers as arguments.")

if __name__ == '__main__':
    unittest.main()