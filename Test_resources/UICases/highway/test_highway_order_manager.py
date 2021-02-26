# coding=utf-8

import unittest
from selenium import webdriver
from Base.browser_engine import BrowserEngine
from PageObjects.highway_homepage import LoginHomepage, IndexHomepage, OrderManagerHomepage
from Base.base_page import BasePage
from Base.FuncApi.api_funcs import get_user_info
import time
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
        order_manage_page = OrderManagerHomepage(self.driver)

        # 登陆
        login_page.input_username('admin')
        login_page.input_password('123456')
        login_page.click_button_login()
        # 进入商品管理页

        index_page.click_list_order_manage()
        # 按照订单号查询
        index_page.switch_first_iframe()
        order_manage_page.input_input_order_number(get_user_info())
        order_manage_page.click_button_select_order()
        order_manage_page.drag_to_right()
        order_manage_page.drag_to_right_list()
        order_manage_page.click_button_check_order()








