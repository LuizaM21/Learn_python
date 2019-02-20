"""
    Read data from config.xml file
    Representing local paths for different file
"""
from lxml import etree
import os
import pprint
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

    def read_from_config_file(self):
        config_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), CONFIGFILE)

        if os.path.isfile(config_file) and config_file.__sizeof__():
            try:
                with open(config_file) as cf:
                    # exclude returned attributes from the returned xml
                    xml_into_dict = xmltodict.parse(cf.read(), attr_prefix='', cdata_key='')
                    # pprint.pprint(xml_into_dict)
                    return xml_into_dict
            except Exception as e:
                return str(e)
        else:
            print("File {} not found".format(self.CONFIGFILE))

    def get_value(self):
        """
        :param dict_key: return a desired value from the valid dictionary defined as constants
        :return: "" string is the parameter value is not found
        """
        if self._paramDict.__contains__(self):
            return self._paramDict.get(self)
        return ""


if __name__ == "__main__":
    ordered_dict = dict(ConfigData().read_from_config_file())
    pprint.pprint(ordered_dict.get("config"))
    print(type(ordered_dict))
