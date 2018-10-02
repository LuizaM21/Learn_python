from BCM_UI.config.ChromeWebDriver import new_browser
import time


class BcmClient:
    def __init__(self,
                 url: object = None,
                 width: object = None,
                 height: object = None,
                 web_driver_file_path: object = None,
                 driver: object = None) -> object:
        if driver is None:
            driver = self._new_bcm_browser(url, width, height, web_driver_file_path)
        self._driver = driver

    @staticmethod
    def _new_bcm_browser(url, width, height, web_driver_file_path):
        chrome_driver = new_browser(url, width, height, web_driver_file_path)
        time.sleep(2)
        return chrome_driver


    def navigate_back(self):
        self._driver.back()