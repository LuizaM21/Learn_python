"""
    Read data from config.xml file
    Representing local paths for different file
"""
import xmltodict
import os
from Python_files_manipulation.FileManipulation import FileManipulation
from Python_files_manipulation.JSONManipulation import JSONManipulation

CONFIGFILE = "config.xml"
BASE_TAG = "config"

# xml parent tags
INPUT_DIR = "input_dir"
OUTPUT_DIR = "output_dir"
CONFIG_MAPPING = {}

# xml child tags
CONFIG_INPUT_LIST = ["input_csv_file", "input_json_file", "input_xml_file", "input_other_file"]
CONFIG_OUTPUT_LIST = ["output_csv_file", "output_json_file", "output_xml_file", "output_other_file"]

# create an expected dictionary formed by expected xml tabs
input_lis = CONFIG_MAPPING.setdefault(INPUT_DIR, CONFIG_INPUT_LIST)
output_lis = CONFIG_MAPPING.setdefault(OUTPUT_DIR, CONFIG_OUTPUT_LIST)


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
        self._paramDict = {}
        self.read_from_config_file()
        self._parse_config_parent_tag()

    def read_from_config_file(self):
        config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), CONFIGFILE)
        config_ok = True

        if os.path.isfile(config_file) and config_file.__sizeof__():
            try:
                with open(config_file) as cf:
                    # exclude returned attributes from the returned xml
                    xml_into_dict = xmltodict.parse(cf.read(), attr_prefix='', cdata_key='')
                    if not xml_into_dict.__contains__(BASE_TAG):
                        print("readConfigFile method missing base tag {}".format(BASE_TAG))
                        return False
                    for parent_tag in CONFIG_MAPPING.keys():
                        print("CONFIG_MAPPING.keys():\n", xml_into_dict[BASE_TAG])
                        resultErrorCode = self._parse_config_parent_tag(xml_into_dict[BASE_TAG], parent_tag)
                        if not resultErrorCode:
                            config_ok = False
                print("Config params successfully read: \n%s", self._paramDict)
            except Exception as e:
                config_ok = False
                return str(e)
        else:
            print("File {} not found".format(self.CONFIGFILE))
        if not config_ok:
            print("Please verify that your config file contains "
                  "all the expected keys under the base tag")

    def _parse_config_parent_tag(self, doc, parent_tag):
        """
        :param doc the entire xml structure in a dictionary format
        :param parent_tag BASE_TAB child including other child division of the xml
        :return result code :
        """
        result_code = True
        if not doc.__contains__(parent_tag):
            print("The tag {} is missing from input file".format(parent_tag))
            result_code = False
            return result_code

        actual_dict_key = doc.get(parent_tag)
        expected_dict_key = CONFIG_MAPPING.get(parent_tag)

        for exp_key in expected_dict_key:
            if actual_dict_key.__contains__(exp_key):
                self._paramDict[exp_key] = actual_dict_key.get(exp_key)
            else:
                print("Expected key: {} is missing from the file ".format(exp_key))
                result_code = False
        return result_code

    def get_value(self):
        """
        :param dict_key: return a desired value from the valid dictionary defined as constants
        :return: "" string is the parameter value is not found
        """
        if self._paramDict.__contains__(self):
            return self._paramDict.get(self)
        return ""


if __name__ == "__main__":
    xml_doc = ConfigData.read_from_config_file("")
    print(xml_doc)
    csv_file = CONFIG_INPUT_LIST[0]
    print(csv_file)
    # print(ConfigData.get_value(csv_file))
    # JSONManipulation.pretty_print_json_data(xml_doc)
    print("Expected dictionary tab values")
    JSONManipulation.pretty_print_json_data(CONFIG_MAPPING)
