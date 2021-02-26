# coding=utf-8

import unittest
from Base.browser_engine import BrowserEngine
from PageObjects.highway_homepage import LoginHomepage, IndexHomepage, ArticleManageHomepage
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
        article_page = ArticleManageHomepage(self.driver)

        # 登陆
        login_page.input_username('admin')
        login_page.input_password('123456')
        login_page.click_button_login()
        # 进入文章管理页
        index_page.click_list_article_manage()
        index_page.switch_first_iframe()
        article_page.click_insert_publish_content()
        self.switch_to_default_content()
        article_page.switch_to_frame_insert_article()
        article_page.click_select_article_type()
        article_page.click_select_article_type_hot()
        article_page.input_input_article_title('ZhrAutoTestArticleTitle')
        article_page.input_input_article_body('ZhrAutoTestArticleBody')
        article_page.click_button_save_article()









