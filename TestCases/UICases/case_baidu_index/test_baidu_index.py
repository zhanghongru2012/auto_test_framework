# coding=utf-8

import unittest
from Base.browser_engine import BrowserEngine
from PageObjects.page_baidu.baidu_homepage import IndexHomePage
from Base.base_page import BasePage
from Base.retry_func import retry_method, retry_class


@retry_class(3)
class TestOaReceiveDocument(unittest.TestCase, BasePage):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_recv_process(self):
        index_page = IndexHomePage(self.driver)
        index_page.type_search('python')
        index_page.send_submit_btn()
        self.assertEqual(1, 1)   # 随便写了个断言，只是个示例，请按实际情况来写断言


if __name__ == '__main__':
    unittest.main()
