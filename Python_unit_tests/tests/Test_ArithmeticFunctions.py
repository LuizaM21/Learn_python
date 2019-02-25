""" to run test only for this file run the following command:
pytest Python_unit_tests/tests/test_ArithmeticFunctions.py -v
"""

import pytest
from Python_algorithms_and_functions.ArithmeticFunctions import ArithmeticFunctions


class TestArithmeticFunctions:

    @pytest.mark.parametrize('test_add_input, exp_add_result', [(ArithmeticFunctions(3, 4).add_two_numbers(), 7),
                                                                (ArithmeticFunctions(1, 1).add_two_numbers(), 2),
                                                                (ArithmeticFunctions(0, 0).add_two_numbers(), 0)])
    def test_add_function(self, test_add_input, exp_add_result):
        assert test_add_input == exp_add_result

    @pytest.mark.parametrize('test_diff_input, exp_diff_result',
                             [(ArithmeticFunctions(3, 4).subtract_two_numbers(), -1),
                              (ArithmeticFunctions(-3, -4).subtract_two_numbers(), 1),
                              (ArithmeticFunctions(-3, 3).subtract_two_numbers(), -6),
                              (
                                      ArithmeticFunctions(-3, 0).subtract_two_numbers(), -3)])
    def test_diff_function(self, test_diff_input, exp_diff_result):
        assert test_diff_input == exp_diff_result

    @pytest.mark.parametrize('test_multiply_input, exp_multiply_result',
                             [(ArithmeticFunctions(3, 4).multiply_two_numbers(), 12),
                              (ArithmeticFunctions(-3, -4).multiply_two_numbers(), 12),
                              (ArithmeticFunctions(-3, 3).multiply_two_numbers(), -9),
                              (ArithmeticFunctions(0, -0).multiply_two_numbers(), 0)])
    def test_multiply_function(self, test_multiply_input, exp_multiply_result):
        assert test_multiply_input == exp_multiply_result

    @pytest.mark.parametrize('test_input, expected_result', [(ArithmeticFunctions(3, 6).divide_two_numbers(), 0.5),
                                                             (ArithmeticFunctions(-3, -4).divide_two_numbers(), 0.75),
                                                             (ArithmeticFunctions(4, 2).divide_two_numbers(), 2),
                                                             (ArithmeticFunctions(-3, -3).divide_two_numbers(), 1),
                                                             (str(ArithmeticFunctions(1, 0).divide_two_numbers()),
                                                              'division by zero')])
    def test_divide_function(self, test_input, expected_result):
        assert test_input == expected_result

    @pytest.mark.parametrize('test_input, expected_result', [(ArithmeticFunctions(5, 3).modulus_of_two_numbers(), 2),
                                                             (ArithmeticFunctions(5, 3).modulus_of_two_numbers(), 2),
                                                             (str(ArithmeticFunctions(5, 0).modulus_of_two_numbers()),
                                                              'cannot divide by zero',)])
    def test_modulo_function(self, test_input, expected_result):
        assert test_input == expected_result

    @pytest.mark.parametrize('test_input, expected_result', [(ArithmeticFunctions(5, 3).exponent_of_two_numbers(), 125),
                                                             (ArithmeticFunctions(5, 0).exponent_of_two_numbers(), 1),
                                                             (
                                                                     ArithmeticFunctions(5,
                                                                                         -1).exponent_of_two_numbers(),
                                                                     0.2),
                                                             (ArithmeticFunctions(5, -2).exponent_of_two_numbers(),
                                                              0.04),
                                                             (ArithmeticFunctions(0, 1).exponent_of_two_numbers(), 0)])
    def test_exponent_function(self, test_input, expected_result):
        assert test_input == expected_result

    @pytest.mark.parametrize('test_input, expected_result', [(ArithmeticFunctions(8, 2).square_root(), 64),
                                                             (ArithmeticFunctions(8, 0).square_root(), 1)])
    def test_square_root_function(self, test_input, expected_result):
        assert test_input == expected_result
