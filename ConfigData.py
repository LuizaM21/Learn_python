"""
    Read data from config.xml file
    Representing local paths for different file
"""

import os
import pprint
from xml.etree import ElementTree as ET


# collect the current path where ConfigData.py is running
PROJECT_DIRECTORY_PATH = os.path.dirname(os.path.realpath(__file__))

CONFIGFILE = "config.xml"

# file keys
OUTPUT_XML_FILE = "output_xml_file"
OUTPUT_COUNTRY_CONFIG_COPY = "output_country_config_copy"
OUTPUT_JSON_FOLDER = "output_json_folder"
OUTPUT_COUNTRY_CONF_COL_COPY = "output_country_conf_col_copy"
OUTPUT_OTHER_FILE = "output_other_file"
SITE_LIST_CSV = "site_list_csv"
COUNTRY_LIST = "country_list"
BREAKFAST_MENU_XML = "breakfast_menu_xml"
SUN_AND_MOON_JPG = "sun_and_moon_jpg"
COUNTRY_CONFIG_CSV = "country_config_csv"
CD_CATALOG_XML = "cd_catalog_xml"
OUTPUT_COUNTRY_LIST_CSV = "output_country_list_csv"
QUIZ_JSON = "quiz_json"
ALL_COUNTRIES_JSON = "all_countries_json"


class ConfigData:
    config = None

    @staticmethod
    def get_instance():
        """
        Verifies if an instance is already created, otherwise create one and store it,
        to avoid multiple reads of the same file
        :return: ConfigData.config instance
        """
        if not ConfigData.config:
            ConfigData.config = ConfigData()
        return ConfigData.config

    def __init__(self):
        self.paramDict = {}
        self.config_file = os.path.join(PROJECT_DIRECTORY_PATH, CONFIGFILE)
        self.read_from_config_file()

    def read_from_config_file(self):
        if os.path.isfile(self.config_file) and os.stat(self.config_file).st_size != 0:
            try:
                # read config file and load the content as a xml object
                xml_content = ET.parse(self.config_file)
                root = xml_content.getroot()
                # collect relative path for input files
                project_files = root[0][0:] + root[1][0:]
                for file in project_files:
                    item = os.path.join(PROJECT_DIRECTORY_PATH, file.text)
                    self.paramDict.setdefault(file.tag, item)
                return self.paramDict
            except Exception as e:
                return str(e)
        else:
            print("File {} not found".format(CONFIGFILE))
            return ""

    def get_value(self, param_key):
        """
        :param param_key: return a desired value from the valid dictionary defined as constants
        :return: "" string if the parameter value is not found
        """
        if param_key and self.paramDict.__contains__(param_key):
            return str(self.paramDict.get(param_key))
        print("Parameter {} not found!".format(param_key))
        return ""


if __name__ == "__main__":

    localConfig = ConfigData.get_instance()
    otherConfig = ConfigData.get_instance()
    print("localConfig instance == otherConfig instance:\n" + str(localConfig == otherConfig))
    config_xml_dict = ConfigData().read_from_config_file()
    pprint.pprint(config_xml_dict)
    print(ConfigData().get_value(OUTPUT_JSON_FOLDER))

