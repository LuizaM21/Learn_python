from selenium import webdriver
from .constants import *


def new_browser(url="http://google.com", width=1280, height=800, web_driver_file_path=WEB_DRIVER_PATH):
    chrome_driver = webdriver.Chrome(web_driver_file_path)
    chrome_driver.get(url)
    chrome_driver.set_window_size(width, height)
    return chrome_driver

