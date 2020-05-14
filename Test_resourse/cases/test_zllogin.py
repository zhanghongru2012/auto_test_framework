# coding=utf-8
import time
from selenium import webdriver
import unittest
from Base.browser_engine import BrowserEngine
from PageObjects.First_homepage import ZL_HomePage
from Base.base_page import BasePage


class ZL_Login(unittest.TestCase, BasePage):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_ZlLlogin(self):
        home_page = ZL_HomePage(self.driver)
        home_page.input_user("yctest")
        home_page.input_passwd("123456")
        home_page.submit_login()
        try:
            user = home_page.get_user()
            assert user == "禹城测试"
            print("登录成功")
        except Exception as e:
            print('登录失败', format(e))


if __name__ == '__main__':
    unittest.main()