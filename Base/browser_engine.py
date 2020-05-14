# -*- coding:utf-8 -*-
import configparser
import os.path
from selenium import webdriver
from Base.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):
    dir = os.path.abspath('.') + '\Test_resourse'
    # 当前版本：81.0.4044.138
    chrome_driver_path = dir + '\Tools\chromedriver.exe'

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, driver):
        config = configparser.ConfigParser()
        file_path = self.dir + '\Configs\config.ini'
        config.read(file_path, encoding='UTF-8')
        browser = config.get("browserType", "browserName")
        url = config.get("server", "URL")
        if browser == "Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)

        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def quit_browser(self):
        self.driver.quit()