import os
from pprint import pprint
import json
"""
Read data from config.json file and store them into a dictionary 
"""

#file keys
ENVINRONMENT = 'environment'
RESOURCE_TYPE = 'resourceType'
METRIC_TYPE = 'metricType'
REGION = 'region'

BASTION_HOST = 'bastion_host'
BASTION_USERNAME = 'bastion_username'
BASTION_KEYFILE = 'bastion_key_file'
BASTION_KEYPASS = 'bastion_keypass'
START_TIME = 'startTime'
END_TIME = 'endTime'
CONFIGFILE = "config.json"

# collect the current path where ConfigData.py is running
PROJECT_DIRECTORY_PATH = os.path.dirname(os.path.realpath(__file__))


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
                # read config file and load the content as a json object
                with open(self.config_file) as f:
                    data = json.load(f)
                    for item in data['config']['aws_server']:
                        self.paramDict.update(item)
                    for item in data['config']['bastion']:
                        self.paramDict.update(item)
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
    config_data = ConfigData()
    data = config_data.read_from_config_file()
    print('REGION = ', config_data.get_value(REGION))
    pprint(data)