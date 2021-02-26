# coding=utf-8

import unittest
from selenium import webdriver
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
        # 进入品类管理页
        index_page.click_list_category_manage()
        # 按照订单号查询
        index_page.switch_first_iframe()
        category_page.click_button_insert_model()
        self.switch_to_default_content()
        category_page.switch_to_frame_insert_model()
        category_page.input_input_model_name('ZhrAutoTestModel')
        category_page.click_radio_if_open_country_level()
        category_page.input_upload_pic_country_level(pic_path + 'many.jpg')
        category_page.click_begin_upload_pic_country_level()
        self.switch_to_default_content()
        category_page.click_known_upload_pic_country_level()
        category_page.switch_to_frame_insert_model()
        category_page.click_button_save_category()







