from collections import OrderedDict
from pprint import pprint as pp
from Python_algorithms_and_functions.SortingAlgorithm import SortingAlgorithm as sortAlg


"""------------------Dictionaries action that can be applied------------------------------------------"""
# create a dictionary
cat_dict = {'name': 'cat', 'age': 3, 'gender': 'female', 'colors': ['black', 'white', 'brown', 'yellow']}
# output keys and values
print('\n' + str(cat_dict.keys()))
print(cat_dict.values())
# get a specific element from the dictionary accessing a specific key
print(cat_dict['name'])
print(cat_dict.get('gender'))
print(cat_dict.get('owner', 'not found!'))
# introduce new element into the dictionary
cat_dict['owner'] = 'Katie'


"""-----------------------Dict pop/del/update/len------------------------------------------"""
print(cat_dict)
# delete the last element of the dictionary
cat_dict.pop('colors')
# delete specific element of the dictionary
del cat_dict['name']
print(cat_dict)
# update existent values and introduce new ones into dictionary
cat_dict.update({'name': 'kitty', 'age': 2, 'paws': 4, 'colors': ['black', 'white']})
print(cat_dict)
# display the length of the dictionary
print(len(cat_dict))
print(cat_dict.items())
# loop into dictionary
sortAlg.iterate_a_list(cat_dict.items())


"""------transform list of tuples into dictionary--------------"""
name_and_ages = [('Alice', 32), ('Tom', 23), ('Charlie', 27), ('Daniel', 33)]
d = dict(name_and_ages)
pp(d)
print('Transform list of tuples into dictionary:\n' + str(d))
avionic_alphabet = dict(a='alpha', b='bravo', c='charlie', d='delta', e='echo')
print('avionic alphabet\n' + str(avionic_alphabet))


"""------extend dictionary using update method---------------"""
avionic_alphabet.update(f='foxtrot')
print('avionic_alphabet updated\n' + str(avionic_alphabet))
for key, value in avionic_alphabet.items():
    print('key: {}  value: {}'.format(key, value))


"""-----------find element in dictionary based by key----------"""
print('a' in avionic_alphabet)
print('r' in avionic_alphabet)


"""-----------------dictionary comprehension-----------------"""
county_to_capital = {'England': 'London', 'Romania': 'Bucharest', 'Greece': 'Athene', 'Turkey': 'Ankara'}
print(county_to_capital)

capital_to_country = {capital: country for country, capital in county_to_capital.items()}
pp(capital_to_country)

alphabet_dict = {'a': 'ALPHA', 'b': 'BETA', 'c': 'CHARLIE', 'd': 'DELTA'}
print('unsorted dictionary')
print(alphabet_dict)
alphabet_dict = OrderedDict().fromkeys('abcd', True)
print('sorted dictionary using OrderedDict')
print(alphabet_dict)


"""-----------------create dict in dict-----------------------"""

basket_1 = {'apples': 3, 'nuts': 5, 'vegetables': 6}
print("BEFORE basket_1 ", basket_1)
basket_2 = {'red': 1, 'green': 2, 'yellow': 3}
basket_1['apples'] = basket_2
print("AFTER basket_1 ", basket_1)

