# coding=utf-8

import unittest
from Base.browser_engine import BrowserEngine
from PageObjects.gly_zy_homepage import LoginHomepage, DealTask, IndexHomepage, AdjustReportEvent
from Base.base_page import BasePage
import time
import os
from Base.retry_func import retry_method, retry_class


@retry_class(3)
class TestOaReceiveDocument(unittest.TestCase, BasePage):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_report_road_manager(self):
        pic_path = os.path.abspath('.') + '\Test_resources\images\\'
        home_page = LoginHomepage(self.driver)
        index_page = IndexHomepage(self.driver)
        adjust_page = AdjustReportEvent(self.driver)
        deal_task = DealTask(self.driver)

        home_page.input_input_user("zytest")
        home_page.input_input_pwd("123456")
        home_page.click_button_login()
        index_page.click_tab_adjust()
        index_page.click_tab_adjust_report_event()
        adjust_page.switch_to_frame_adjust_report_event()
        adjust_page.click_select_event_type()
        adjust_page.click_select_td_event_type_btsd()
        adjust_page.click_select_check_team()
        adjust_page.click_select_td_check_team1()
        adjust_page.input_input_event_content('事件描述')
        adjust_page.click_select_on_road()
        adjust_page.click_select_on_road_x050()
        adjust_page.click_select_up_down()
        adjust_page.click_select_up_down_up()
        adjust_page.input_input_begin_zh('15')
        adjust_page.input_input_end_zh('16')
        adjust_page.input_upload_pic(pic_path + 'many.jpg')

        adjust_page.click_button_begin_upload_pic()
        self.switch_to_default_content()
        adjust_page.click_button_known_upload_pic()
        adjust_page.switch_to_frame_adjust_report_event()
        adjust_page.click_button_save()
        self.switch_to_default_content()
        adjust_page.click_button_save_success_known()
        adjust_page.switch_to_frame_adjust_report_event()
        adjust_page.click_button_submit()


if __name__ == '__main__':
    unittest.main()
