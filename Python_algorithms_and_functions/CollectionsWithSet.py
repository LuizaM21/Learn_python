"""unordered collection od unique immutable objects
order is arbitrary"""

from Python_algorithms_and_functions.SortingAlgorithm import SortingAlgorithm as sortAlg


"""------------------Set type action that can be applied------------------------------------------"""
# this list will throw away duplicate values
# sets will retrieve a new element order each run-time
months_1_set_list = {'january', 'february', 'march', 'april', 'may', 'june', 'july', 'july'}
months_2_set_list = {'july', 'august', 'september', 'october', 'november', 'december', 'january'}
sortAlg.check_value_in_array('april', months_1_set_list)
print('\nSet list 1:\n' + str(months_1_set_list))
print('\nSet list 2:\n' + str(months_2_set_list))


"""------------------Set union/remove/discard/add/copy------------------------------------------"""
# merge two set list
months_set_list_united = months_1_set_list.union(months_2_set_list)
print('\nNew copied Set list:\n' + str(months_set_list_united))
sortAlg.iterate_a_list(months_set_list_united)
# copy list into an empty one
years = months_set_list_united.copy()
print('\nYear = copied list:\n' + str(years))
# remove an element from the set list
months_set_list_united.remove('january')
months_set_list_united.discard('june')
months_set_list_united.pop()
sortAlg.iterate_a_list(months_set_list_united)
# add element o the set list
months_set_list_united.add('october')


"""-------------------Set intersection/difference/is disjoint----------------------------------"""
print('\nSet list with NO january and june:\n' + str(months_set_list_united))
print('Verify if element is present in set:\n' + str('january' in months_set_list_united))
print('Common values between 2 set list\n' + str(months_1_set_list.intersection(months_2_set_list)))
print('Differences between two set list\n' + str(months_2_set_list.difference(months_1_set_list)))
# verify if 2 sets have common value between them
print('Sets lists are disjointed: ' + str(months_1_set_list.isdisjoint(months_2_set_list)))

# create an empty set using the set constructor
set_list = set()
print(type(set_list))

""" transform list into set values using set constructor
frequently used when we want to remove duplicate values from a list"""
code_list = [3, 4, 3, 87, 87, 32, 1, 22, 2, 2]
s = set(code_list)
print(s)

# check if common elements form two sets exists using subset method
print(str(months_1_set_list.issubset(months_2_set_list)))

# check two sets have no members in common
print(months_1_set_list.isdisjoint(months_2_set_list))


"""------------------------------set comprehensions-----------------------------------------"""
""" For each iterable item on the right evaluate the expression on the left
The comprehension is included in curly braces for set types"""

year = {year.capitalize() for year in years}
print('---------------Set comprehension------------------')
print(year)
























