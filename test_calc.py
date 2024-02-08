test contents
def test_large_number_addition():
    assert calculate('+', 999999999, 1) == 1000000000

def test_large_number_multiplication():
    assert calculate('*', 100000000, 100000000) == 10000000000000000

def test_overflow_scenario():
    # This test assumes the calculator app has a maximum value it can handle
    max_value = 1e+308  # Example maximum value, adjust based on the app's actual limit
    assert calculate('+', max_value, 1) == "Error: Value exceeds maximum limit.