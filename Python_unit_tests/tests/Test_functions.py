"""To run the pyTest write in terminal the cmd:
pytest Python_unit_tests/tests/test_functions.py -v
"""
from Python_algorithms_and_functions.ArithmeticFunctions import ArithmeticFunctions


def test_sum_of_elem():
    result = ArithmeticFunctions(2, 4).add_two_numbers()
    assert result == 6


def test_subtract_function():
    result = ArithmeticFunctions(20, 4).subtract_two_numbers()
    assert result == 16


def test_list():
    list_one = [1, 2, 3]
    list_two = [2, 3, 4]
    assert len(list_one) == len(list_two)



