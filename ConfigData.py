"""
    Read data from config.xml file
    Representing local paths for different file
"""


class ConfigData:
    config = None

    @staticmethod
    def get_instance():
        if not ConfigData.config:
            ConfigData.config = ConfigData()
        return ConfigData.config

