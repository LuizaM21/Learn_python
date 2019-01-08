import sys
import pprint
from pathlib import Path

from Python_files_manipulation.CSVManipulation import CSVManipulation
from Python_files_manipulation.FileManipulation import FileManipulation
from Python_files_manipulation.JSONManipulation import JSONManipulation

global_folder_path = Path('C:\Learning_Python_Scripts\Python_project_files')

all_countries_json = global_folder_path / 'Input_files\JSON_files\GetAllCountries.json'
quiz_file = global_folder_path / 'Input_files\JSON_files\quiz.json'

country_config_csv = global_folder_path / 'Input_files\CSV_files\CountryConfig.csv'
country_config_csv_copy = global_folder_path / 'Output_files\CSV_files\CountryConfig_copy.csv'
CountryConfig_columns_copy = global_folder_path / 'Output_files\CSV_files\CountryConfig_columns_copy.csv'
country_list_output = global_folder_path / 'Output_files\CSV_files\CountryList.csv'

binary_file = global_folder_path / 'Input_files\OTHER_files\sun_and_moon.jpg'
binary_file_copy = global_folder_path / 'Output_files\OTHER_files\sun_and_moon_copy.jpg'


if __name__ == "__main__":
    json_obj = JSONManipulation(quiz_file).read_json_file()
    pprint.pprint(json_obj)
    file_m_obj = FileManipulation(country_config_csv)
    output_file = file_m_obj.read_file()
    print(output_file)
    words_number = file_m_obj.count_words()
    print("Total words in file = ", words_number)

    write_to_file = FileManipulation(country_list_output).write_file()
    print(write_to_file)

    copy_into_file = FileManipulation(country_config_csv).copy_text_file(country_config_csv_copy)
    print(copy_into_file)
    append_info_into_existent_file = FileManipulation(country_list_output).add_to_existent_file()
    print(append_info_into_existent_file)

    fh_jpg = FileManipulation(binary_file).copy_binary_file(binary_file_copy)
    print(fh_jpg)

    csv_m = CSVManipulation(country_config_csv, country_config_csv_copy)
    csv_m.read_csv_specific_column(3)
    csv_m.copy_csv_column_into_new_file(3)

    csv_dict = CSVManipulation(country_config_csv, CountryConfig_columns_copy)
    csv_dict.read_csv_as_dictionary('CapitalCity')
    csv_dict.write_csv_as_dictionary()
    sys.exit()


