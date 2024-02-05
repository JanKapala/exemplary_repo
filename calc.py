"""
Simple command-line calculator app named 'calc'.
Usage: python calc.py [operation] [arg1] [arg2]
Supported operations: +, -, *, /
"""

import sys

def calculate(operation, arg1, arg2):
    if operation == '+':
        return arg1 + arg2
    elif operation == '-':
        return arg1 - arg2
    elif operation == '*':
        return arg1 * arg2
    elif operation == '/':
        try:
            return arg1 / arg2
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    else:
        return "Unsupported operation."

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python calc.py [operation] [arg1] [arg2]")
    else:
        _, operation, arg1, arg2 = sys.argv
        try:
            arg1 = float(arg1)
            arg2 = float(arg2)
            result = calculate(operation, arg1, arg2)
            print(f"Result: {result}")
        except ValueError:
            print("Error: Please provide valid numbers as arguments.")