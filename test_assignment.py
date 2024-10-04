import pytest
import inspect
from assignment import nth_power, reverse_number, binary_to_decimal

def check_contains_loop(function):
    source = inspect.getsource(function)
    return 'for' in source or 'while' in source

@pytest.mark.parametrize("base, exponent, expected", [
    (3, 4, 81),
    (5, 2, 25),
    (10, 5, 100000),
    (2, 10, 1024),
    (7, 0, 1)
])
def test1(base, exponent, expected):
    assert nth_power(base, exponent) == expected
    assert check_contains_loop(nth_power)

@pytest.mark.parametrize("input, expected", [
    (1234, 4321),
    (19283, 38291),
    (1, 1),
    (987654, 456789),
    (0, 0)
])
def test2(input, expected):
    assert reverse_number(input) == expected
    assert check_contains_loop(reverse_number)

@pytest.mark.parametrize("binary_input, expected", [
    (1010, 10),
    (110111, 55),
    (11111111, 255),
    (100000, 32),
    (0, 0)
])
def test3(binary_input, expected):
    assert binary_to_decimal(binary_input) == expected
    assert check_contains_loop(binary_to_decimal)  
