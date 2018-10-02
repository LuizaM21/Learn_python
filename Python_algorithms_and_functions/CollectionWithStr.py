"""str is a immutable sequence of Unicode characters"""


# determine the length of a string using build in function
alphabet = 'alphabet'
print(len(alphabet))
# concatenate a string using + sign
double_words = alphabet + alphabet
print(len(double_words))

country_1 = 'Antigua And Barbuda'
country_2 = 'Bosnia And Herzegovina'
"""--------------------join()-------------------------"""
# concatenate string using join() method
# more efficient
countries = ', '.join([country_1, country_2])
print(countries)

"""--------------------split()-------------------------"""
# transform str into a list using split() method
country_list = countries.split(',')
print(country_list)
print(type(country_list))

"""--------------------partition()-------------------------"""
# once applied on a str return a tuple of values
# usually used on unpacking tuples
file_name = 'FileNameYYYYMMDDtime.csv'
print(file_name)
# unpack a tuple
(f_name, f_date, f_time) = file_name.partition('YYYYMMDD')
print('file_name: ' + f_name + '\n',
      'file_date: ' + f_date + '\n',
      'file_time: ' + f_time)

"""--------------------format()-------------------------"""
# format method can be called with replacement fields defined by {}
print('\nfile_name: {0}\nfile_date: {1}\nfile_time: {2}'.format(f_name, f_date, f_time))
print('entire file name: {file_n}'.format(file_n=file_name))

# access value through key or indexes
position = (65.3, 45.2, 78.3)
print('position coordinates x={pos[0]}, y{pos[1]}, z={pos[2]}'.format(pos=position))


