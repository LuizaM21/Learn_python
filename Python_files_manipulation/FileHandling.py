import sys

from Python_files_manipulation.CSVManipulation import CSVManipulation
from Python_files_manipulation.FileManipulation import FileManipulation
from Python_files_manipulation.JSONManipulation import JSONManipulation


fh_json = FileManipulation('GetAllCountries.json', 'GetAllCountries2.json')

fh_json.read_file()
fh_json.write_file()
fh_json.copy_text_file()
fh_json.add_to_existent_file()

fh_jpg = FileManipulation('sun_and_moon.jpg', 'sun_and_moon_copy.jpg')

fh_jpg.copy_binary_file()

csv_m = CSVManipulation('CountryConfig.csv', 'CountryConfig_copy.csv')

csv_m.read_csv_specific_column(3)
csv_m.copy_csv_column_into_new_file(3)

csv_dict = CSVManipulation('CountryConfig.csv', 'CountryConfig_columns_copy.csv')

csv_dict.read_csv_as_dictionary('CapitalCity')
csv_dict.write_csv_as_dictionary()

# json_m = JSONManipulation('GetAllCountries.json')
# json_m.read_json_file()


if __name__ == "__main__":
    fh_json.read_file()
    sys.exit()
