import sys


def check_palindrome(input_value):
    """"Check if the value is a palindrome"""

    word = reversed(input_value)
    if list(word) == list(input_value):
        print("Input: {} is a palindrome ".format(input_value))
        return True
    else:
        print("Input: {} is not a palindrome".format(input_value))
        return False


def calculate_sum_of_numbers(*numbers):
    """"Calculate the sum of the entered parameters"""
    try:
        isinstance(numbers, list)
        input_num = [int(in_num) for in_num in numbers]
        print("The sum of the elements is: ", sum(input_num))
        return sum(input_num)
    except ValueError:
        print(ValueError)


def check_prime_number(input_num):
    """Check if a number is prime or not"""

    try:
        int(input_num)
        if input_num % 2 != 0 or input_num == 2:
            print("Number {} is prime".format(input_num))
            return True
        else:
            print("Number {} is not prime because it doesnt`t divide only by itself and value 1".format(input_num))
            return False
    except ValueError as val_er:
        print(val_er)
        return False


def calculate_inputs(input_one, operand, input_two):
    if isinstance(input_one, int) and isinstance(input_two, int):
        try:
            if operand == "+":
                print("For operand {} result is: {}".format(operand, input_one + input_two))
                return input_one + input_two
            if operand == "-":
                print("For operand {} result is: {}".format(operand, input_one - input_two))
                return input_one - input_two
            if operand == "*":
                print("For operand {} result is: {}".format(operand, input_one * input_two))
                return input_one * input_two
            if operand == "/":
                print("For operand {} result is: {}".format(operand, input_one / input_two))
                return input_one / input_two
            if operand == "%":
                print("For operand {} result is: {}".format(operand, input_one % input_two))
                return input_one / input_two
            if operand == "**":
                print("For operand {} result is: {}".format(operand, input_one ** input_two))
                return input_one ** input_two
            else:
                print("No known operand")
                return False
        except ValueError as val_err:
            print(val_err)
            return False


def no_operation(* _):
    """For non-valid operations"""
    print("{} is not a known command. Please try the following commands: {}".format((sys.argv[1]),
          ", ".join(tuxy_commands.keys())))


tuxy_commands = {
    "palindrome": check_palindrome,
    "calculate_sum": calculate_sum_of_numbers,
    "prime_num": check_prime_number,
    "calculate_inputs": calculate_inputs}


def main():
    """Commands for Tuxy robot"""
    if len(sys.argv) == 1:
        print("The current method is: {} <command>".format(sys.argv[0]))
        print(sys.argv)
        return
    print(sys.argv)
    command = tuxy_commands.get(sys.argv[1], no_operation)
    command(*sys.argv[2:])


if __name__ == "__main__":
    main()
    calculate_inputs(3, "%", 2)
    # calculate_two_operators(2,+,2)
    # assert check_prime_number(5)
    # assert check_prime_number(3)
    # assert check_prime_number(5)
    # assert not check_prime_number(12)
    # assert not check_prime_number(4)
    # assert check_palindrome((1, 2, 2, 1))
    # assert not check_palindrome("wantsome")
    # calculate_sum_of_numbers(1, 2, 3, 4, 5)
    # assert calculate_sum_of_numbers(1, 2, 3) == 6

