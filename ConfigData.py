"""
    Read data from config.xml file
    Representing local paths for different file
"""
import xmltodict
from pathlib import Path
from Python_files_manipulation.FileManipulation import FileManipulation
from Python_files_manipulation.JSONManipulation import JSONManipulation
projectPath = Path('C:\Learning_Python_Scripts')
CONFIGFILE = 'config.xml'

BASE_TAG = "config"

# xml parent tags
INPUT_DIR = "input_dir"
OUTPUT_DIR = "output_dir"
CONFIG_MAPPING = {}

# xml child tags
INPUT_CSV_FILE = "input_csv_file"
INPUT_JSON_FILE = "input_json_file"
INPUT_OTHER_FILE = "input_other_file"

OUTPUT_CSV_FILE = "output_csv_file"
OUTPUT_JSON_FILE = "output_json_file"
OUTPUT_OTHER_FILE = "output_other_file"

# create an expected dictionary formed by expected xml tabs
CONFIG_INPUT_LIST = [INPUT_CSV_FILE, INPUT_JSON_FILE, INPUT_OTHER_FILE]
CONFIG_MAPPING.update({INPUT_DIR: CONFIG_INPUT_LIST})

CONFIG_OUTPUT_LIST = [OUTPUT_CSV_FILE, OUTPUT_JSON_FILE, OUTPUT_OTHER_FILE]
CONFIG_MAPPING.update({OUTPUT_DIR: CONFIG_OUTPUT_LIST})


class ConfigData:
    config = None

    @staticmethod
    def get_instance():
        if not ConfigData.config:
            ConfigData.config = ConfigData()
        return ConfigData.config

    def __init__(self):
        self.read_from_config_file()

    @staticmethod
    def read_from_config_file():
        config_file = projectPath / CONFIGFILE
        if config_file.exists() and config_file.__sizeof__():
            try:
                con_file = FileManipulation(config_file).read_file()
                doc = xmltodict.parse(con_file)
                JSONManipulation.pretty_print_json_data(doc)
                return doc
            except Exception as e:
                return str(e)
        else:
            print("File {} not found".format(CONFIGFILE))


if __name__ == "__main__":
    ConfigData.read_from_config_file()

    print("Expected dictionary tab values")
    JSONManipulation.pretty_print_json_data(CONFIG_MAPPING)
