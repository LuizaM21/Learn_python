import math
import sys


class ArithmeticFunctions:

    def add_two_numbers(self, num2):
        result = int(self) + int(num2)
        print('Sum of two numbers: ' + str(result))
        return result

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
    ArithmeticFunctions.add_two_numbers(2, 3)
    ArithmeticFunctions.complete_two_cities("Craiova", "Iasi")
    sys.exit()

