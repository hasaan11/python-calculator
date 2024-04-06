import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from calc import addition, subtraction, multiplication, division



@pytest.fixture
def setup_data():
    # Setup code
    data = {"num1": 5, "num2": 3}
    yield data  # Provide data to test functions
    # Teardown code (optional)

# Test addition function
@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 8),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_addition(num1, num2, expected):
    assert addition(num1, num2) == expected

# Test subtraction function
@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 2),
    (1, -1, 2),
    (0, 0, 0),
])
def test_subtraction(num1, num2, expected):
    assert subtraction(num1, num2) == expected

# Test multiplication function
@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 15),
    (0, 10, 0),
    (-1, -1, 1),
])
def test_multiplication(num1, num2, expected):
    assert multiplication(num1, num2) == expected

# Test division function
@pytest.mark.parametrize("num1, num2, expected", [
    (6, 3, 2),
    (10, 2, 5),
    (-10, 2, -5),
])
def test_division(num1, num2, expected):
    assert division(num1, num2) == expected

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        division(5, 0)

