# coding=utf-8

import unittest
from Base.browser_engine import BrowserEngine
from PageObjects.highway_homepage import LoginHomepage, IndexHomepage, GoodsManager, InsertGoods
from Base.base_page import BasePage
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
        goods_page = GoodsManager(self.driver)
        insert_good_page = InsertGoods(self.driver)
        # 登陆
        login_page.input_username('admin')
        login_page.input_password('123456')
        login_page.click_button_login()
        # 进入商品管理页
        index_page.click_list_good_manage()
        # 进入添加商品管理页
        insert_good_page.switch_to_frame_goods_manager()
        insert_good_page.click_button_insert_good()
        self.switch_to_default_content()
        insert_good_page.switch_to_frame_insert_good_step1()
        insert_good_page.input_input_goods_name('zhr-api-autotest')
        insert_good_page.input_upload_goods_main_pic(pic_path + 'many.jpg')
        insert_good_page.click_begin_upload_goods_main_pic()
        self.switch_to_default_content()
        insert_good_page.click_known_upload_goods_main_pic()
        insert_good_page.switch_to_frame_insert_good_step1()
        insert_good_page.input_upload_goods_many_pic(pic_path + 'many.jpg')
        insert_good_page.click_begin_upload_goods_many_pic()
        self.switch_to_default_content()
        insert_good_page.click_known_upload_goods_many_pic()
        insert_good_page.switch_to_frame_insert_good_step1()
        insert_good_page.click_select_category()
        insert_good_page.click_select_category_highway()
        insert_good_page.click_select_model_zhr()
        insert_good_page.input_input_packing_method('zzz')
        insert_good_page.input_input_place_of_origin('zzz')
        insert_good_page.input_input_company('zzz')
        insert_good_page.input_input_test_index('zzz')
        insert_good_page.input_input_shelf_life('100')
        insert_good_page.click_choose_if_import()
        insert_good_page.click_choose_if_on_shelf()
        insert_good_page.click_button_next_step_to_step2()

        self.switch_to_default_content()
        insert_good_page.switch_to_frame_insert_good_step2()
        insert_good_page.click_select_brand()
        insert_good_page.click_select_brand_choose_zhr()
        insert_good_page.click_select_supplier()
        insert_good_page.click_select_supplier_choose_zhr()
        insert_good_page.click_select_supplier_choose_zhr_close()
        insert_good_page.input_input_price('100')
        insert_good_page.input_input_stock('100')
        insert_good_page.input_upload_model_pic(pic_path + 'many.jpg')
        insert_good_page.click_begin_upload_model_pic()
        self.switch_to_default_content()
        insert_good_page.click_known_upload_model_pic()
        insert_good_page.switch_to_frame_insert_good_step2()
        insert_good_page.click_button_over_insert_good()
        self.switch_to_default_content()
        a = insert_good_page.get_text_success_text()
        insert_good_page.click_list_area_of_goods()
        # self.assertEqual('保存成功', a)





