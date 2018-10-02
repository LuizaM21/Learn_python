"""Unhandled exections will terminate the program """
import sys
from math import log


def convert_to_int(s):
    """Handle multiple exception in a single try except block"""
    try:
        return int(s)
        print('Conversion succeeded! for item {}'.format(s))
    # exception accepts tuple of errors type
    except (ValueError, TypeError) as exp:
        print("Conversion failed for item {}: {}"
              .format(s, str(exp)), file=sys.stderr)  # print message to the standard error stream
        raise


def string_log(x):
    v = convert_to_int(x)
    return log(v)


def square_root(x):
    # Heron`s method
    if x < 0:
        raise ValueError("Cannot compute square root of {}".format(x))
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def divide_two_numbers(div_one, div_two):
    """use finally statement to execute functionality even if error are handle"""
    try:
        result = div_one / div_two
    except ZeroDivisionError:
        print("cannot divide by zero!")
    except TypeError:
        print("arguments must be int not str or list!")
    else:
        print("division results = ", result)
    finally:
        print("Executing final clause\n")


if __name__ == "__main__":
    divide_two_numbers(9, 3)
    divide_two_numbers('star', 3)
    divide_two_numbers('star', 0)
    divide_two_numbers(0, 0)
    sys.exit()
    try:
        print(square_root(9))
        print(square_root(2))
        print(square_root(-1))
    except ValueError as e:
        print(e, file=sys.stderr)

    number_type = convert_to_int("2")
    print(type(number_type))

    string_type = convert_to_int("test")
    print(string_type)

    list_type = convert_to_int([1, 2, 5, 7])
    print(type(list_type))

    string_test = string_log("test")
    print(string_test)



