# coding=utf-8

import unittest
from Base.browser_engine import BrowserEngine
from PageObjects.highway_homepage import LoginHomepage, IndexHomepage, CategoryManageHomepage
from Base.base_page import BasePage
import os
from Base.retry_func import retry_method, retry_class


# @retry_class(3)
class TestCaseSuit(unittest.TestCase, BasePage):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_goods_manager(self):
        pic_path = os.path.abspath('..') + '\Test_resources\images\\'
        print(pic_path)
        login_page = LoginHomepage(self.driver)
        index_page = IndexHomepage(self.driver)
        category_page = CategoryManageHomepage(self.driver)

        # 登陆
        login_page.input_username('admin')
        login_page.input_password('123456')
        login_page.click_button_login()







