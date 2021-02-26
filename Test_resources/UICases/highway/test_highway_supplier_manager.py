# coding=utf-8

import unittest
from selenium import webdriver
from Base.browser_engine import BrowserEngine
from PageObjects.highway_homepage import LoginHomepage, IndexHomepage, SupplierManageHomepage
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
        supplier_page = SupplierManageHomepage(self.driver)

        # 登陆
        login_page.input_username('admin')
        login_page.input_password('123456')
        login_page.click_button_login()
        index_page.click_list_supplier_manage()
        index_page.switch_first_iframe()
        supplier_page.click_button_insert_supplier()
        self.switch_to_default_content()
        supplier_page.switch_to_frame_insert_supplier()
        supplier_page.input_input_supplier_name('zzz')
        supplier_page.input_input_supplier_address('zzz')
        supplier_page.input_input_supplier_person('zzz')
        supplier_page.input_input_supplier_tel('18888888888')
        supplier_page.click_radio_select_category_choose_highway_material()
        supplier_page.click_select_brand()
        supplier_page.click_select_brand_zhr()
        supplier_page.click_select_brand_close()
        supplier_page.click_button_save_supplier()









