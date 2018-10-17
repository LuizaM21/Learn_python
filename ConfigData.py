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
CONFIG_INPUT_LIST = ["input_csv_file", "input_json_file", "input_xml_file", "input_other_file"]
CONFIG_OUTPUT_LIST = ["output_csv_file", "output_json_file", "output_xml_file", "output_other_file"]

# create an expected dictionary formed by expected xml tabs
CONFIG_MAPPING.update({INPUT_DIR: CONFIG_INPUT_LIST})
CONFIG_MAPPING.update({OUTPUT_DIR: CONFIG_OUTPUT_LIST})


class ConfigData:
    config = None

    @staticmethod
    def get_instance():
        """
        Verifies if an instance is already created, otherwise create one and store it,
        to avoid multiple reads of the same file
        :return: ConfigData instance
        """
        if not ConfigData.config:
            ConfigData.config = ConfigData()
        return ConfigData.config

    def __init__(self):
        self.read_from_config_file()
        self._paramDict = {}

    def read_from_config_file(self):
        config_file = projectPath / CONFIGFILE
        if config_file.exists() and config_file.__sizeof__():
            try:
                conf_file = FileManipulation(config_file).read_file()
                xml_into_dict = xmltodict.parse(conf_file, attr_prefix='', cdata_key='')
                if not xml_into_dict.__contains__(BASE_TAG):
                    print("missing base tag {}".format(BASE_TAG))
                    return False
                for parent_tag in CONFIG_MAPPING.keys():
                    self._parse_config_parent_tag(xml_into_dict[BASE_TAG], parent_tag)
                return xml_into_dict
            except Exception as e:
                return str(e)
        else:
            print("File {} not found".format(CONFIGFILE))

    def _parse_config_parent_tag(self, doc, parent_tag):
        """
        :param doc the entire xml structure in a dictionary format
        :param parent_tag BASE_TAB child including other child division of the xml
        :return result code :
        """
        MISSING_ERROR_CODE = -1
        EXTRA_ERROR_CODE = 1
        ACTUAL_RESULT_CODE = 0

        if not doc.__contains__(parent_tag):
            print("The tag {} is missing from input file".format(parent_tag))
            return MISSING_ERROR_CODE

        actual_dict_key = doc.get(parent_tag)
        expected_dict_key = CONFIG_MAPPING.get(parent_tag)

        if actual_dict_key.keys().__len__() > expected_dict_key.__len__():
            print("File has more config keys! Expected {0} Actual {1}".format(expected_dict_key.__len__(),
                                                                              actual_dict_key.keys().__len__()))
            ACTUAL_RESULT_CODE = EXTRA_ERROR_CODE

        if actual_dict_key.keys().__len__() < expected_dict_key.__len__():
            print("File has less config keys! Expected {0} Actual {1}".format(expected_dict_key.__len__(),
                                                                              actual_dict_key.keys().__len__()))
            ACTUAL_RESULT_CODE = MISSING_ERROR_CODE

        for expected_key in expected_dict_key:
            if actual_dict_key.__contains__(expected_key):
                self._paramDict[expected_key] = actual_dict_key.get(expected_key)
            else:
                print("Expected key: {} is missing from the file ".format(expected_key))
                ACTUAL_RESULT_CODE = MISSING_ERROR_CODE
        return ACTUAL_RESULT_CODE

    def get_value(self, dict_key):
        """
        :param dict_key: return a desired value from the valid dictionary defined as constants
        :return: "" string is the parameter value is not found
        """
        if self._paramDict.__contains__(dict_key):
            return self._paramDict.get(dict_key)
        return ""


if __name__ == "__main__":
    xml_doc = ConfigData.read_from_config_file("")
    print(xml_doc)
    print(ConfigData.get_value(CONFIG_INPUT_LIST[0]))
    # JSONManipulation.pretty_print_json_data(xml_doc)
    print("Expected dictionary tab values")
    JSONManipulation.pretty_print_json_data(CONFIG_MAPPING)
