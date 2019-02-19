import sys
import os

from Python_files_manipulation.CSVManipulation import CSVManipulation
from Python_files_manipulation.FileManipulation import FileManipulation
from Python_files_manipulation.JSONManipulation import JSONManipulation

global_folder_path = os.path.dirname(os.path.realpath(__file__))
dynamic_path = os.path.split(global_folder_path)
current_path = dynamic_path[0]

COUNTRY_CONFIG_CSV = os.path.join(str(current_path), 'Python_project_files\Input_files\CSV_files\CountryConfig.csv')
COUNTRY_CONFIG_CSV_COPY = os.path.join(str(current_path), 'Python_project_files\Output_files\CSV_files'
                                                          '\CountryConfig_copy'
                                                          '.csv')
COUNTRY_CONF_COL_COPY = os.path.join(str(current_path), 'Python_project_files\Output_files\CSV_files'
                                                        '\CountryConfig_columns_copy.csv')
COUNTRY_OUTPUT_FILE = os.path.join(str(current_path), 'Python_project_files\Output_files\CSV_files\CountryList.csv')

BINARY_FILE = os.path.join(str(current_path), 'Python_project_files\Input_files\OTHER_files\sun_and_moon.jpg')
BINARY_FILE_COPY = os.path.join(str(current_path),
                                "Python_project_files\Output_files\OTHER_files\sun_and_moon_copy.jpg")

if __name__ == "__main__":
    copy_into_file = FileManipulation(COUNTRY_CONFIG_CSV).copy_text_file(COUNTRY_CONFIG_CSV_COPY)
    data_content = FileManipulation(COUNTRY_CONFIG_CSV).read_file()
    print(data_content)
    append_info_into_existent_file = FileManipulation(COUNTRY_OUTPUT_FILE).add_to_existent_file()
    print(append_info_into_existent_file)

    # fh_jpg = FileManipulation(BINARY_FILE).copy_binary_file(BINARY_FILE_COPY)
    # print(fh_jpg)

    # csv_m = CSVManipulation(country_config_csv, country_config_csv_copy)
    # csv_m.read_csv_specific_column(3)
    # csv_m.copy_csv_column_into_new_file(3)

    # csv_dict = CSVManipulation(country_config_csv, CountryConfig_columns_copy)
    # csv_dict.read_csv_as_dictionary('CapitalCity')
    # # csv_dict.write_csv_as_dictionary()
    sys.exit()
