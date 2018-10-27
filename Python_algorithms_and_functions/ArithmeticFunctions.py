import math
import sys


class ArithmeticFunctions:

    def add_two_numbers(self, num2):
        result = int(self) + int(num2)
        print('Sum of two numbers: ' + str(result))
        return result

    @staticmethod
    def gaseste_unic(number_list):
        single_val = set()
        for num in number_list:
            if num not in single_val:
                single_val.add(num)
            else:
                single_val.remove(num)
        return int(str(single_val).replace("{", "").replace("}", ""))



    @staticmethod
    def prim(numar):
        """Funcție ce determină dacă un număr este prim."""
        if numar < 2:
            return False
        elif numar != 2 and numar % 2 == 0:
            return False
        else:
            return True

    @staticmethod
    def par(number):
        """Funcție ce determină dacă un număr este par sau nu"""
        if number % 2 == 0:
            print("Number %d is even" % number)
            return True
        else:
            print("Number %d is odd" % number)
            return False

    @staticmethod
    def maxim(num1, num2):
        """Funcție ce determină maximul dintre două numere."""
        # Funcția va returna maximul dintre cele două numere
        if num1 > num2:
            max_value = num1
            print("number {} is greater than number {}".format(max_value, num2))
            return max_value
        elif num1 < num2:
            max_value = num2
            print("number {} is greater than number {}".format(max_value, num1))
            return max_value
        else:
            max_value = num2
            print("number {} is equal with number {}".format(max_value, num2))
            return max_value

    @staticmethod
    def minim(num1, num2):
        """Funcție ce determină minimul dintre două numere."""
        # Funcția va returna minimul dintre cele două numere
        if num1 > num2:
            min_value = num2
            print("number {} is lower than number {}".format(min_value, num1))
            return min_value
        elif num1 < num2:
            min_value = num1
            print("number {} is lower than number {}".format(min_value, num2))
            return min_value
        else:
            min_value = num2
            print("number {} is equal with number {}".format(min_value, num2))
            return min_value

    @staticmethod
    def is_palindrome(str_pal):
        """Funcție ce determină dacă șirul primit este palindrom."""
        word = reversed(str_pal)
        if list(word) == list(str_pal):
            print("word {} is a palindrome ".format(str_pal))
            return True
        else:
            print("word: {} is not a palindrome".format(str_pal))
            return False

    @staticmethod
    def is_pow_of(n):
        if n == 0:
            return False
        while n != 1:
            if n % 2 != 0:
                return False
            n = n // 2
        return True

    @staticmethod
    def factorial_of(num):
        factorial = 1
        if num < 0:
            return False
        elif num == 0:
            return 1
        else:
            for i in range(factorial, num + 1):
                factorial = factorial * i
            print("Final Factorial result: %d " % factorial)
            return factorial

    @staticmethod
    def numar_vocale(word):
        """Determina numarul de vocale."""
        number_vowel = 0
        char_list = list(word.lower())
        vocale = ('a', 'e', 'i', 'o', 'u')
        for char in char_list:
            if char in vocale:
                number_vowel += 1
        return number_vowel

    @staticmethod
    def cuvinte(propozitie):
        """Determina numarul de cuvinte."""
        word_counter = len(propozitie.split(" "))
        return word_counter

    def subtract_two_numbers(self, num2):
        result = self - num2
        print('Subtraction of two numbers: ' + str(result))
        return result

    def multiply_two_numbers(self, num2):
        result = self * num2
        print('Multiplication of two numbers: ' + str(result))
        return result

    def divide_two_numbers(self, divider):
        """ Catch exception if zero value is given"""
        try:
            result = self / divider
        except Exception as e:
            print('divider was zero')
            return e
        else:
            print('Division of two numbers: ' + str(result))
        return result

    def modulus_of_two_numbers(self, num2):
        if num2 == 0:
            print('divider value is zero')
            return 'cannot divide by zero'
        result = self % num2
        print('Modulus of two numbers: ' + str(result))
        return result

    def exponent_of_two_numbers(self, num2):
        results = self ** num2

        print('Exponent of two numbers: ' + str(results))
        return results

    def square_root(self, exponent):
        result = math.pow(self, exponent)
        print('Math.pow function applied on two numbers: ' + str(result))
        return result

    def square(self):
        return self * self

    def map_function(self, arg_list):
        """function that takes as parameter another function but without parenthesis
            This will execute the function without expecting any parameters"""
        items = []
        for i in arg_list:
            items.append(self(i))
        return items

    squares = map_function(square, [1, 2, 3, 4])
    print(squares)

    def decorator_function(self):
        def wrapper_function(*args, **kwargs):
            print("Romania is default country")
            return self(*args, **kwargs)
        return wrapper_function

    @decorator_function
    def complete_country_with_city(self):
        print('Iasi city')

    @decorator_function
    def complete_two_cities(self, city):
        print('{} and {} '.format(self, city) + 'cities')

    complete_country_with_city()
    complete_two_cities('Bucuresti', 'Cluj')


if __name__ == '__main__':
    ArithmeticFunctions.par(3)
    ArithmeticFunctions.maxim(2, 3)
    ArithmeticFunctions.maxim(5, 3)
    ArithmeticFunctions.maxim(3, 3)
    assert ArithmeticFunctions.minim(2, 4) == 2
    assert ArithmeticFunctions.minim(4, 3) == 3
    assert ArithmeticFunctions.minim(2, 2) == 2
    assert not ArithmeticFunctions.is_palindrome("car")
    assert ArithmeticFunctions.is_palindrome("tacocat")
    assert (ArithmeticFunctions.is_pow_of(2))
    assert (ArithmeticFunctions.is_pow_of(8))
    assert (ArithmeticFunctions.is_pow_of(32))
    assert not (ArithmeticFunctions.is_pow_of(10))
    assert not (ArithmeticFunctions.is_pow_of(25))
    ArithmeticFunctions.factorial_of(3)
    ArithmeticFunctions.factorial_of(5)
    ArithmeticFunctions.factorial_of(0)
    ArithmeticFunctions.factorial_of(1)
    assert ArithmeticFunctions.numar_vocale("asap") == 2
    assert ArithmeticFunctions.numar_vocale("asaaap") == 4
    assert ArithmeticFunctions.cuvinte("Ana are mere.") == 3
    assert ArithmeticFunctions.cuvinte("Incepe sa imi placa Python.") == 5
    print(ArithmeticFunctions.prim(3))
    print(ArithmeticFunctions.prim(100151))
    assert ArithmeticFunctions.gaseste_unic([1, 1, 2, 3, 2]) == 3
    assert ArithmeticFunctions.gaseste_unic([1, 1, 2, 2, 1]) == 1
    assert ArithmeticFunctions.gaseste_unic([1, 1, 1, 2, 2]) == 1
    ArithmeticFunctions.add_two_numbers(2, 3)
    ArithmeticFunctions.complete_two_cities("Craiova", "Iasi")
    sys.exit()

