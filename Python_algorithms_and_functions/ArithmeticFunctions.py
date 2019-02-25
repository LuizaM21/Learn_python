import math
import sys
import functools


def decorator_function(input_function):
    @functools.wraps(input_function)
    def wrapper_function(*args, **kwargs):
        print("Romania is default country")
        value = input_function(*args, **kwargs)
        return value
    return wrapper_function


class ArithmeticFunctions:
    def __init__(self, val1, val2=None):
        self.val_1 = val1
        self.val_2 = val2

    def add_two_numbers(self):
        result = int(self.val_1) + int(self.val_2)
        print('Sum of two numbers: ' + str(result))
        return result

    def subtract_two_numbers(self):
        result = self.val_1 - self.val_2
        print('Subtraction of two numbers: ' + str(result))
        return result

    def find_unique_number(self):
        single_val = set()
        for num in self.val_1:
            if num not in single_val:
                single_val.add(num)
            else:
                single_val.remove(num)
        return int(str(single_val).replace("{", "").replace("}", ""))

    def check_prime_num(self):
        """Analyze if a number is prime or not"""
        if self.val_1 < 2:
            return False
        elif self.val_1 != 2 and self.val_1 % 2 == 0:
            return False
        else:
            return True

    def detect_even_or_odd_num(self):
        """Function to determine is a number is even or not"""
        if self.val_1 % 2 == 0:
            print("Number %d is even" % self.val_1)
            return True
        else:
            print("Number %d is odd" % self.val_1)
            return False

    def maxim(self):
        """Determine maximum value from two numbers"""
        if self.val_1 > self.val_2:
            max_value = self.val_1
            print("Number {} is greater than number {}".format(max_value, self.val_2))
            return max_value
        elif self.val_1 < self.val_2:
            max_value = self.val_2
            print("Number {} is greater than number {}".format(max_value, self.val_1))
            return max_value
        else:
            max_value = self.val_2
            print("Number {} is equal with number {}".format(max_value, self.val_2))
            return max_value

    def minim(self):
        """Determine minimum value from two numbers"""
        if self.val_1 > self.val_2:
            min_value = self.val_2
            print("number {} is lower than number {}".format(min_value, self.val_1))
            return min_value
        elif self.val_1 < self.val_2:
            min_value = self.val_1
            print("number {} is lower than number {}".format(min_value, self.val_2))
            return min_value
        else:
            min_value = self.val_2
            print("number {} is equal with number {}".format(min_value, self.val_2))
            return min_value

    def is_palindrome(self):
        """Determine if the input is palindrome or not"""
        word = reversed(self.val_1)
        if list(word) == list(self.val_1):
            print("word {} is a palindrome ".format(self.val_1))
            return True
        else:
            print("word: {} is not a palindrome".format(self.val_1))
            return False

    def is_pow_of(self):
        if self.val_1 == 0:
            return False
        while self.val_1 != 1:
            if self.val_1 % 2 != 0:
                return False
            self.val_1 = self.val_1 // 2
        return True

    def factorial_of(self):
        factorial = 1
        if self.val_1 < 0:
            return False
        elif self.val_1 == 0:
            return 1
        else:
            for i in range(factorial, self.val_1 + 1):
                factorial = factorial * i
            print("Final Factorial result: %d " % factorial)
            return factorial

    def count_vocals(self):
        """Return the number of vocals from a word"""
        number_vowel = 0
        char_list = list(self.val_1.lower())
        vocals = ('a', 'e', 'i', 'o', 'u')
        for char in char_list:
            if char in vocals:
                number_vowel += 1
        return number_vowel

    def count_word_from_sentence(self):
        """Return the number of words from a sentence"""
        word_counter = len(self.val_1.split(" "))
        return word_counter

    def multiply_two_numbers(self):
        result = self.val_1 * self.val_2
        print('Multiplication of two numbers: ' + str(result))
        return result

    def divide_two_numbers(self):
        """ Catch exception if zero value is given"""
        try:
            result = self.val_1 / self.val_2
        except Exception as e:
            print('divider was zero')
            return e
        else:
            print('Division of two numbers: ' + str(result))
        return result

    def modulus_of_two_numbers(self):
        if self.val_2 == 0:
            print('divider value is zero')
            return 'cannot divide by zero'
        result = self.val_1 % self.val_2
        print('Modulus of two numbers: ' + str(result))
        return result

    def exponent_of_two_numbers(self):
        results = self.val_1 ** self.val_2
        print('Exponent of two numbers: ' + str(results))
        return results

    def square_root(self):
        result = math.pow(self.val_1, self.val_2)
        print('Math.pow function applied on two numbers: ' + str(result))
        return result

    def square(self):
        return self.val_1 * self.val_1

    @staticmethod
    @decorator_function
    def complete_two_cities(*city):
        print('{} and {} '.format(city[0], city[1]) + 'cities')


if __name__ == '__main__':

    ArithmeticFunctions.complete_two_cities('Bucuresti', 'Cluj')
    ArithmeticFunctions.complete_two_cities("Craiova", "Iasi")
    ArithmeticFunctions(2).detect_even_or_odd_num()
    ArithmeticFunctions(2, 3).maxim()
    ArithmeticFunctions(5, 3).maxim()
    ArithmeticFunctions(3, 3).maxim()
    square_root = ArithmeticFunctions(2).square()
    print(square_root)
    assert ArithmeticFunctions(2, 4).minim() == 2
    assert ArithmeticFunctions(4, 3).minim() == 3
    assert ArithmeticFunctions(2, 2).minim() == 2
    assert not ArithmeticFunctions("car").is_palindrome()
    assert ArithmeticFunctions("tacocat").is_palindrome()
    assert ArithmeticFunctions(2).is_pow_of()
    assert ArithmeticFunctions(8).is_pow_of()
    assert ArithmeticFunctions(32).is_pow_of()
    assert not ArithmeticFunctions(10).is_pow_of()
    assert not ArithmeticFunctions(25).is_pow_of()
    ArithmeticFunctions(3).factorial_of()
    ArithmeticFunctions(5).factorial_of()
    ArithmeticFunctions(0).factorial_of()
    ArithmeticFunctions(1).factorial_of()
    assert ArithmeticFunctions("asap").count_vocals() == 2
    assert ArithmeticFunctions("asaaap").count_vocals() == 4
    assert ArithmeticFunctions("Ana are mere.").count_word_from_sentence() == 3
    assert ArithmeticFunctions("Check this sentence").count_word_from_sentence() == 3
    print(ArithmeticFunctions(3).check_prime_num())
    print(ArithmeticFunctions(100151).check_prime_num())
    assert ArithmeticFunctions([1, 1, 2, 3, 2]).find_unique_number() == 3
    assert ArithmeticFunctions([1, 1, 2, 2, 1]).find_unique_number() == 1
    assert ArithmeticFunctions([1, 1, 1, 2, 2]).find_unique_number() == 1
    ArithmeticFunctions(2, 3).add_two_numbers()
    sys.exit()

