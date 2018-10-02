

class SortingAlgorithm:

    """----------------Iterate a vector---------------"""
    def iterate_a_list(self):
        for index, item in enumerate(self, start=1):
            print([index], item)

    def sort_vector(self):
        print("\n")
        self.sort()
        return self

    @staticmethod
    def find_thee_number_in_list():
        print("----Iterator and decision statements----------------")
        number_list = [1, 2, 3, 4, 5, 6, 7, 8]
        for num in number_list:
            if num == 3:
                print('Found ' + str(num), end=" ")
                continue
            if num == 7:
                break
            print(num, end=" ")
        print('\n')

    @staticmethod
    def display_odd_and_even_numbers():
        print("Display odd and even number in range of 1 to 10 ")
        for i in range(0, 11):
            if (i % 2) == 0:
                print('EVEN: ' + str(i), end=" ")
            else:
                print('ODD: ' + str(i), end=" ")
        print()

    @staticmethod
    def display_five_numbers_applying_while_loop():
        x = 0
        print('\nApply while loop')
        while True:
            if x == 5:
                break
            print(x, end=" ")
            x += 1
        print()

    """------------Create conditional functions-----------------"""
    def compare_two_values(self, value_2):
        if self < value_2:
            return print(str(value_2) + " is bigger than value " + str(self))
        elif self > value_2:
            return print(str(self) + " is bigger than value " + str(value_2))
        else:
            return print(str(self) + " is equal with " + str(value_2))

    def check_value_in_array(self, array=list()):
        if self not in array:
            return print('\n' + str(self) + ' is not present in array')
        else:
            return print('\n' + str(self) + ' is present in array')


if __name__ == '__main__':
    """------------------Display Functions output---------------"""
    SortingAlgorithm.compare_two_values(3, 4)
    SortingAlgorithm.compare_two_values(3, 3)
    SortingAlgorithm.compare_two_values(4, 1)

