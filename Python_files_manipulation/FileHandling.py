import sys
from pathlib import Path

from Python_files_manipulation.CSVManipulation import CSVManipulation
from Python_files_manipulation.FileManipulation import FileManipulation
from Python_files_manipulation.JSONManipulation import JSONManipulation

global_folder_path = Path('C:\Learning_Python_Scripts\Python_files_manipulation')
all_countries_json = global_folder_path / 'GetAllCountries.json'
quiz_file = global_folder_path / 'quiz.json'
country_config_csv = 'CountryConfig.csv'


if __name__ == "__main__":
    json_obj = JSONManipulation(quiz_file).read_json_file()
    print(json_obj)
    file_m_obj = FileManipulation(country_config_csv)
    output_file = file_m_obj.read_file()
    print(output_file)

    write_to_file = FileManipulation('CountryList.csv').write_file()
    print(write_to_file)

    copy_into_file = FileManipulation(country_config_csv).copy_text_file('CountryConfig_copy.csv')
    print(copy_into_file)
    append_info_into_existent_file = FileManipulation('CountryList.csv').add_to_existent_file()
    print(append_info_into_existent_file)
    sys.exit()

    fh_jpg = FileManipulation('sun_and_moon.jpg', 'sun_and_moon_copy.jpg')
    fh_jpg.copy_binary_file()

    csv_m = CSVManipulation('CountryConfig.csv', 'CountryConfig_copy.csv')
    csv_m.read_csv_specific_column(3)
    csv_m.copy_csv_column_into_new_file(3)

    csv_dict = CSVManipulation('CountryConfig.csv', 'CountryConfig_columns_copy.csv')
    csv_dict.read_csv_as_dictionary('CapitalCity')
    csv_dict.write_csv_as_dictionary()


