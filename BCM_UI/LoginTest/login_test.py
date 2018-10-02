from BCM_UI.base import TestBase
from BCM_UI.config import ChromeWebDriver
from ..config.constants import *

CONFIG_DATA = get_config_from_json('config_automation')


class TestLogin(TestBase):

    @classmethod
    def setup_class(cls):
        if "browser settings" in CONFIG_DATA:
            cls._browser_settings = CONFIG_DATA["browser settings"]

    def setup_method(self, test_method):
        super().setup_method(self, test_method)

