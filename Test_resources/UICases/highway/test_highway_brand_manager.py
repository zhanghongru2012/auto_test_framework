# coding=utf-8

import unittest
from selenium import webdriver
from Base.browser_engine import BrowserEngine
from PageObjects.highway_homepage import LoginHomepage, IndexHomepage, BrandManageHomepage
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
        login_page = LoginHomepage(self.driver)
        index_page = IndexHomepage(self.driver)
        brand_page = BrandManageHomepage(self.driver)

        # 登陆
        login_page.input_username('admin')
        login_page.input_password('123456')
        login_page.click_button_login()
        # 进入品牌管理页
        index_page.click_list_brand_manage()
        index_page.switch_first_iframe()
        brand_page.click_button_insert_brand()
        self.switch_to_default_content()
        brand_page.switch_to_frame_insert_brand()
        brand_page.input_input_brand_name('ZhrAutoTestBrandName')
        brand_page.click_radio_select_category()
        brand_page.click_select_model()
        brand_page.click_select_model_zhr()
        brand_page.click_select_model_close()
        brand_page.click_button_save_brand()








