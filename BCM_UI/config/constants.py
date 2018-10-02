import json
from os import path
from BCM_UI import config


def get_config_from_json(file_name):
    config_dir = path.dirname(config.__file__)
    file_path = path.join(config_dir, file_name)
    return json.loads(open(file_path).read())


default_browser_data = get_config_from_json('config_automation.json')

SCREENSHOT_FOLDER_PATH = default_browser_data['screenshots']['folder_path']
WEB_DRIVER_PATH = default_browser_data['web_driver_file_path']['chrome']
DEFAULT_BROWSER_SETTINGS = default_browser_data['browser settings']
WALL_SETUP = default_browser_data['wall setup']
LOGIN_SETUP = default_browser_data['login']
