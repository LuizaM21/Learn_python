from unittest import TestCase
from Python_algorithms_and_functions.ArithmeticFunctions import ArithmeticFunctions


class BasicTestCase(TestCase):
    def test_first_function(self):
        self.assertEqual(1, 1)

    def test_sum(self):
        result = ArithmeticFunctions(2, 3).add_two_numbers()
        self.assertEqual(5, result, 'check the results of the sum method')

    def test_list(self):
        list_one = [1, 2, 3]
        list_two = [2, 3, 4]
        self.assertEqual(len(list_one), len(list_two))

