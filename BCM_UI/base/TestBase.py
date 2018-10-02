from BCM_UI.config import *
from BCM_UI.base.BcmClient import *


class TestBase:
    _bcm_client = None
    _browser_settings = DEFAULT_BROWSER_SETTINGS
    _web_driver_folder_path = WEB_DRIVER_PATH
    _screenshot_folder_path = SCREENSHOT_FOLDER_PATH

    @property
    def bcm_client(self):
        """
        Returns:
            BcmClient
        """
        return self._bcm_client

    @staticmethod
    def _message(message):
        print("++", message)

    def setup_method(self, method):
        self._bcm_client = BcmClient(**self._browser_settings, web_driver_file_path=self._web_driver_folder_path)
        self._message('opened browser')

    def teardown_method(self, test_method):
        """ closes the browser and removes the factory for page-components """
        self.bcm_client.close_browser()
        self._bcm_client = None
        self._message("closed browser.\n")
