# coding=utf-8
from Base.base_page import BasePage


class IndexHomePage(BasePage):
    """
    维护所有元素和元素可操作方法
    """
    # 输入框1
    input_box = "id=>kw"
    # 百度一下按钮
    search_submit_btn = "xpath=>//*[@id='su']"

    def type_search(self, text):
        self.send_keys(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)
