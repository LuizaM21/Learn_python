import unittest
import operator
import re


class CollectionsOfMethods(unittest.TestCase):
    cities = ["Iasi", "London", "Paris", "Greece"]
    countries = ['Italy', 'Greece', 'England', 'France']
    dict = {'Tim': 18, 'Katie': 35, 'John': 21, 'Nicole': 22}
    ro_counties = {'AG': 'Argeș', 'AR': 'Arad', 'B': 'Bucuresti', 'BC': 'Bacau', 'BH': 'Bihor',
                   'BN': 'Bistrița-Năsăud', 'BR': 'Brăila', 'BT': 'Botoșani', 'BV': 'Brașov', 'BZ': 'Buzău',
                   'CJ': 'Cluj', 'CL': 'Călărași', 'CS':'Caraș-Severin', 'CT':'Constanța', 'CV': 'Covasna',
                   'DB': 'Dâmbovița', 'DJ': 'Dolj', 'GJ': 'Gorj', 'GL': 'Galați', 'GR': 'Giurgiu',
                   'HD': 'Hunedoara', 'HR': 'Harghita', 'IF': 'Ilfov', 'IL':'Ialomița', 'IS': 'Iași',
                   'MH': 'Mehedinți', 'MM': 'Maramureș', 'MS': 'Mureș', 'NT': 'Neamț', 'OT': 'Olt',
                   'PH': 'Prahova', 'SB': 'Sibiu', 'SJ': 'Sălaj', 'SV': 'Suceava', 'SM': 'Satu Mare',
                   'TL': 'Tulcea', 'TM': 'Timiș', 'TR': 'Teleorman', 'VL': 'Vâlcea', 'VN': 'Vrancea', 'VS': 'Vaslui'}

    def sort_vector(self):
        print("\n")
        self.sort()
        return self

    @staticmethod
    def insert_city(city):
        return city

    @staticmethod
    def insert_country(country):
        return '{} country'.format(country)

    @staticmethod
    def validate_car_number(plate_number):
        # create valid dictionary with counties
        ro_counties = {'AG': 'Argeș', 'AR': 'Arad', 'B': 'Bucuresti', 'BC': 'Bacau', 'BH': 'Bihor',
                       'BN': 'Bistrița-Năsăud', 'BR': 'Brăila', 'BT': 'Botoșani', 'BV': 'Brașov', 'BZ': 'Buzău',
                       'CJ': 'Cluj', 'CL': 'Călărași', 'CS':'Caraș-Severin', 'CT':'Constanța', 'CV': 'Covasna',
                       'DB': 'Dâmbovița', 'DJ': 'Dolj', 'GJ': 'Gorj', 'GL': 'Galați', 'GR': 'Giurgiu',
                       'HD': 'Hunedoara', 'HR': 'Harghita', 'IF': 'Ilfov', 'IL':'Ialomița', 'IS': 'Iași',
                       'MH': 'Mehedinți', 'MM': 'Maramureș', 'MS': 'Mureș', 'NT': 'Neamț', 'OT': 'Olt',
                       'PH': 'Prahova', 'SB': 'Sibiu', 'SJ': 'Sălaj', 'SV': 'Suceava', 'SM': 'Satu Mare',
                       'TL': 'Tulcea', 'TM': 'Timiș', 'TR': 'Teleorman', 'VL': 'Vâlcea', 'VN': 'Vrancea', 'VS': 'Vaslui'}

        # extract country acronym from input parameter
        county = plate_number[:2]
        if '-' in county:
            county = list(county)
            county.pop()
            county = ''.join(county)

        # create match pattern for input parameter format
        reg_ex = '((B)-(0[1-9]|[1-9][0-9]|[1-9][0-9][0-9])-([A-Z]{3}))|(([A-Z]{2})-(0[1-9])-([A-Z]{3}))'
        match_plate = re.match(reg_ex, plate_number.upper())

        # verify plate number
        if match_plate:
            if county in ro_counties.keys():
                return True
        else:
            return False

    @staticmethod
    def multiple_arguments(*args, **kwargs):
        """pass multiple data in parameters"""
        print(args)
        print(kwargs)

    def test_multiple_arguments(self):
        courses = ['Math', 'Arts', 'Science']
        student_info = {'name': 'John', 'age': 24, 'study year': 2}
        self.multiple_arguments(*courses, **student_info)

    def test_inserted(self):
        print(str(self.insert_city('\nTokyo')))
        print(self.insert_country('\nChina'))

    def test_city_list(self):
        for city in self.cities:
            print(city)
        self.assertEqual("Iasi", self.cities[0])
        self.assertEqual("London", self.cities[1])

    def test_country_list(self):
        print('\nCheck list length')
        self.assertEqual(4, self.countries.__len__())

    def test_country_France(self):
        print('\nCheck France country')
        self.assertEqual('France', self.countries[3])
        print('%s is in country list ' % self.countries[3])

    def test_dictionary_sorted_by_keys(self):
        print('\ndictionary reverse sort by key')
        sorted_dict = sorted(self.dict.items(), key=operator.itemgetter(0), reverse=True)
        print('%s' % str(sorted_dict))

        # exclude first element from the dictionary
        for key, value in sorted_dict:
            if key == 'John':
                continue
            print('dictionary KEY: %s' % str(key) + ' - VALUE: %s' % str(value))

    def test_plate_number(self):
        self.assertTrue(self.validate_car_number('IS-03-RFS'))
        self.assertFalse(self.validate_car_number('B-23456-RGD'))
        self.assertFalse(self.validate_car_number('AS-56-RGD'))

