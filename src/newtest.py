
import pytest

# Sample function to test
def sum_function(a, b):
    return a + b

@pytest.mark.api
def test_sum_function():
    a, b = 5, 10
    expected_result = 15
    assert sum_function(a, b) == expected_result, f"Expected {expected_result}, but got {sum_function(a, b)}"
