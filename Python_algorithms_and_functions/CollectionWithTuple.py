""" tuple are immutable sequence or arbitrary objects
you can`t modify this type of list
once created, the object within them cannot be replaced or removed"""

import sys
from Python_algorithms_and_functions.SortingAlgorithm import SortingAlgorithm as sortAlg


"""------------------Tuple action that can be applied--------------------------------------------------"""
# pack the tuple
tuple_1 = (1, "january", 30, "spring")
# unpack the tuple
(month_number, month_name, total_days, season) = tuple_1

# create another tuple
tuple_2 = (2, "february", 28, "spring")

# concatenate the 2 tuples in order to create a third one
tuple_3 = tuple_1 + tuple_2
print('\nThird tuple created by added tuples:\n' + str(tuple_3))
print('Check element from the first half:\n' + str('january' in tuple_3))
print('Check element from the second half:\n' + str('february' in tuple_3))

tuple_3 = tuple_1
# create nested tuples
nested_tuple = (tuple_1, tuple_2, tuple_3)

# access inner element of a collection of tuples
inner_elem = nested_tuple[1][1]

# create e tuple with only one element
tuple_4 = (101,)


if __name__ == '__main__':
    sortAlg.check_value_in_array(1, tuple_1)
    sortAlg.check_value_in_array('january', tuple_1)

    print("\nPrint tuple data from tuple 1:\n" + str(tuple_1))
    print("\nPrint first 2 values from the tuple 1:\n" + str(tuple_1[0:2]))

    # call a method from the class iterate with index inside
    sortAlg.iterate_a_list(tuple_3)
    print('Nested tuple:\n' + str(nested_tuple))
    print('Tuple inner element:\n' + str(inner_elem))
    print('tuple with one element' + str(tuple_4))
    # verify if tuple_4 is part of tuple class
    print(type(tuple_4))
    sys.exit()


