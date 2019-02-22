import sys
import pprint

import ConfigData as cd
from Python_files_manipulation.CSVManipulation import CSVManipulation as csv_manipulation
from Python_files_manipulation.FileManipulation import FileManipulation as file_manipulation
from Python_files_manipulation.JSONManipulation import JSONManipulation as json_manipulation

config_data = cd.ConfigData.get_instance()

COUNTRY_CONFIG_CSV = config_data.get_value(cd.COUNTRY_CONFIG_CSV)
COUNTRY_CONFIG_CSV_COPY = config_data.get_value(cd.OUTPUT_COUNTRY_CONFIG_COPY)
COUNTRY_CONF_COL_COPY = config_data.get_value(cd.OUTPUT_COUNTRY_CONF_COL_COPY)
COUNTRY_OUTPUT_FILE = config_data.get_value(cd.OUTPUT_COUNTRY_LIST_CSV)
BINARY_FILE = config_data.get_value(cd.SUN_AND_MOON_JPG)
BINARY_FILE_COPY = config_data.get_value(cd.OUTPUT_OTHER_FILE)
ALL_COUNTRIES_JSON = config_data.get_value(cd.ALL_COUNTRIES_JSON)
QUIZ_JSON = config_data.get_value(cd.QUIZ_JSON)


if __name__ == "__main__":
    copy_into_file = file_manipulation(COUNTRY_CONFIG_CSV).copy_text_file(COUNTRY_CONFIG_CSV_COPY)
    data_content = file_manipulation(COUNTRY_CONFIG_CSV).read_file()
    print(data_content)

    append_info_into_existent_file = file_manipulation(COUNTRY_OUTPUT_FILE).add_to_existent_file()
    print(append_info_into_existent_file)

    fh_jpg = file_manipulation(BINARY_FILE).copy_binary_file(BINARY_FILE_COPY)
    print(fh_jpg)

    csv_m = csv_manipulation(COUNTRY_CONFIG_CSV, COUNTRY_CONFIG_CSV_COPY)
    single_column = csv_m.read_csv_specific_column(3)
    print(single_column)
    csv_m.copy_csv_column_into_new_file(2)

    csv_dict = csv_manipulation(COUNTRY_CONFIG_CSV, COUNTRY_CONF_COL_COPY)
    csv_dict.read_csv_as_dictionary('CapitalCity')
    csv_dict.write_csv_as_dictionary()

    json_file = json_manipulation(QUIZ_JSON).read_json_file()
    pprint.pprint(json_file)
    sys.exit()
