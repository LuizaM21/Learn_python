import pytest

from Python_algorithms_and_functions.ArithmeticFunctions import *


class TestArithmeticFunctions:
    calc = ArithmeticFunctions

    @pytest.mark.parametrize('test_input, expected_result', [(calc.add_two_numbers(3, 4), 7),
                                                             (calc.add_two_numbers(1, 1), 2),
                                                             (calc.add_two_numbers(0, 0), 0)])
    def test_add_function(self, test_input, expected_result):
        assert test_input == expected_result

    @pytest.mark.parametrize('test_input, expected_result', [(calc.subtract_two_numbers(3, 4), -1),
                                                             (calc.subtract_two_numbers(-3, -4), 1),
                                                             (calc.subtract_two_numbers(-3, 3), -6),
                                                             (calc.subtract_two_numbers(-3, 0), -3)])
    def test_diff_function(self, test_input, expected_result):
        assert test_input == expected_result

    @pytest.mark.parametrize('test_input, expected_result', [(calc.multiply_two_numbers(3, 4), 12),
                                                             (calc.multiply_two_numbers(-3, -4), 12),
                                                             (calc.multiply_two_numbers(-3, 3), -9),
                                                             (calc.multiply_two_numbers(0, -0), 0)])
    def test_multiply_function(self, test_input, expected_result):
        assert test_input == expected_result

    @pytest.mark.parametrize('test_input, expected_result', [(calc.divide_two_numbers(3, 6), 0.5),
                                                             (calc.divide_two_numbers(-3, -4), 0.75),
                                                             (calc.divide_two_numbers(4, 2), 2),
                                                             (calc.divide_two_numbers(-3, -3), 1),
                                                             (str(calc.divide_two_numbers(1, 0)), 'division by zero')])
    def test_divide_function(self, test_input, expected_result):
        assert test_input == expected_result

    @pytest.mark.parametrize('test_input, expected_result', [(calc.modulus_of_two_numbers(5, 3), 2),
                                                             (calc.modulus_of_two_numbers(5, 5), 0),
                                                             (str(calc.modulus_of_two_numbers(5, 0)),
                                                              'cannot divide by zero',)])
    def test_modulo_function(self, test_input, expected_result):
        assert test_input == expected_result

    @pytest.mark.parametrize('test_input, expected_result', [(calc.exponent_of_two_numbers(5, 3), 125),
                                                             (calc.exponent_of_two_numbers(5, 0), 1),
                                                             (calc.exponent_of_two_numbers(5, -1), 0.2),
                                                             (calc.exponent_of_two_numbers(5, -2), 0.04),
                                                             (calc.exponent_of_two_numbers(0, 1), 0)])
    def test_exponent_function(self, test_input, expected_result):
        assert test_input == expected_result

    @pytest.mark.parametrize('test_input, expected_result', [(calc.square_root(8, 2), 64),
                                                             (calc.square_root(8, 0), 1)])
    def test_square_root_function(self, test_input, expected_result):
        assert test_input == expected_result


