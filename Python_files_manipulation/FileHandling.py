import sys
import os

from Python_files_manipulation.CSVManipulation import CSVManipulation
from Python_files_manipulation.FileManipulation import FileManipulation
from Python_files_manipulation.JSONManipulation import JSONManipulation

global_folder_path = os.path.dirname(os.path.realpath(__file__))
dynamic_path = os.path.split(global_folder_path)
dynamic_path = dynamic_path[0]

country_config_csv = os.path.join(dynamic_path, 'Python_project_files\Input_files\CSV_files\CountryConfig.csv')
country_config_csv_copy = os.path.join(dynamic_path, 'Python_project_files\Output_files\CSV_files\CountryConfig_copy'
                                                     '.csv')
CountryConfig_columns_copy = os.path.join(dynamic_path, 'Python_project_files\Output_files\CSV_files'
                                                        '\CountryConfig_columns_copy.csv')
country_list_output = os.path.join(dynamic_path, 'Python_project_files\Output_files\CSV_files\CountryList.csv')

binary_file = os.path.join(dynamic_path, 'Python_project_files\Input_files\OTHER_files\sun_and_moon.jpg')
binary_file_copy = os.path.join(dynamic_path, 'Python_project_files\Output_files\OTHER_files\sun_and_moon_copy.jpg')


if __name__ == "__main__":

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
    # csv_dict.write_csv_as_dictionary()
    sys.exit()


