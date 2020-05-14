# coding=utf-8
from Base.base_page import BasePage


class HomePage(BasePage):
    input_box = "id=>kw"
    search_submit_btn = "xpath=>//*[@id='su']"

    def type_search(self, text):
        self.send_keys(self.input_box, text)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)


class ZL_HomePage(BasePage):
    input_username = "id=>user"
    input_password = "id=>password"
    button_login = "class_name=>btn-default"
    user_text = "class_name=>account"

    def input_user(self, text):
        self.send_keys(self.input_username, text)

    def input_passwd(self, text):
        self.send_keys(self.input_password, text)

    def submit_login(self):
        self.click(self.button_login)

    def get_user(self):
        return self.get_text(self.user_text)