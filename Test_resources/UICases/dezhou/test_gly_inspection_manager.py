# coding=utf-8
import unittest
from Base.browser_engine import BrowserEngine
from PageObjects.gly_homepage import LoginHomePage
from Base.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from Base.retry_func import retry_method, retry_class
import time


class TestGlyInspectionManager(unittest.TestCase, BasePage):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        home_page = LoginHomePage(self.driver)
        home_page.input_user("yctest")
        home_page.input_passwd("yantai0535")
        home_page.submit_login()
        try:
            user = home_page.get_user()
            assert user == "禹城测试"
        except Exception as e:
            print('登录失败', format(e))
        # 点击巡查管理
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[4]/div/span[3]"
        ).click()
        # 点击巡查管理-事件上报
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[4]/ul/li[1]/div/span[2]").click()
        # 切入iframe
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/iframe'))
        time.sleep(3)
        print("已切换到iframe, wait a moment")
        # 点击事件细类下拉
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[1]/div[2]/div[3]/div/div[2]/input[1]").click()
        # 选择路基
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span").click()
        # 选择巡查中队
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[1]/div[2]/div[6]/div/div[2]/input[1]").click()
        # 选择一中队
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[4]/span").click()
        # 选择上报人员下拉
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[1]/div[2]/div[9]/div/div[2]/input[1]").click()
        # 选择禹城测试
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[12]/span").click()
        # 事件描述输入
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[1]/div[2]/div[10]/div[2]/textarea").send_keys("事件描述")
        # 应急措施输入
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[1]/div[2]/div[11]/div[2]/textarea").send_keys("应急措施")
        # 维修建议输入
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[1]/div[2]/div[12]/div[2]/textarea").send_keys("维修建议")
        # 所在路线下拉
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/input[1]").click()
        # 选择济南-德州
        try:
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span").click()
        except Exception as e:
            print(e)
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span").click()

        # 选择上下行
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/input[1]").click()
        time.sleep(3)
        # 选择上行
        try:
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span").click()
        except Exception as e:
            print(e)
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span").click()

        # 输入起点桩号
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/input").send_keys("52.522")
        # 输入止点桩号
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[2]/div[2]/div[4]/div[2]/input").send_keys("59.22")
        # 输入偏移量
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[3]/div/div[1]/div/div[2]/div[2]/div[5]/div[2]/input").send_keys("0.07")
        # 上传图片
        up_load = WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((By.XPATH, '//input[@name="file"]')))
        up_load.send_keys("/home/zhanghongru/work/智路/ZL_PyProjects/UITestFramework/Test_resources/Screenshots/timg.jpeg")
        time.sleep(5)
        # 确认上传
        self.driver.find_element_by_xpath('//*[@id="event-uploader_uploader"]/div[1]/div/div[2]').click()
        print("upload success")
        self.driver.switch_to.default_content()
        time.sleep(3)
        # 点击知道了
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button").click()
        print("确认成功")
        # 切入嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/iframe'))
        time.sleep(3)
        # 点击添加路产损坏
        try:
            self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/form/button[1]").click()
        except Exception as e:
            print(e)
            self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div[2]/div[1]/div/div/div[1]/div/div/form/button[1]").click()
        # 切出iframe
        self.driver.switch_to.default_content()
        time.sleep(3)
        # 切入路产损坏iframe
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[11]/div[2]/iframe'))
        time.sleep(3)
        # 选择边沟
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/ul/li/ul/li/ul/li[1]/div").click()
        # 选择土质边沟
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div/span").click()
        # 选择压毁
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[4]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/label/span").click()
        # 点击确定按钮
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/button").click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        time.sleep(3)
        # 切入嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/iframe'))
        time.sleep(3)
        # 点击保存
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[1]/div[1]/button[2]').click()
        print("保存按钮已点击")

        # 跳出嵌套
        self.driver.switch_to.default_content()
        # 找到提示信息并打印, 点击知道了
        tip_text = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[1]/td/p").get_attribute("textContent")
        print(tip_text)
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button").click()
        # 切入嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/iframe'))
        time.sleep(3)
        # 点击提交流程
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div[1]/div/div/form/div[1]/div[1]/button[3]').click()
        print("""
        -------------------- 彩蛋  --------------------
        |                                             |
        |                                             |
        |                  success                    |
        |                                             |
        |                                             |
        --------------------  end  --------------------
        """)

        # 首页用户信息-鼠标悬停
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('user-info')).perform()
        # 工单管理-点击
        WebDriverWait(self.driver,10,0.5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/ul/li[6]/span[2]'))).click()
        print('打开流程管理frame')
        # 最大化流程管理嵌套框
        WebDriverWait(self.driver,10,0.5).until(
            EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'))).click()
        time.sleep(3)
        # 切入流程管理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[11]/div[2]/iframe'))
        time.sleep(3)
        print('已切入流程管理嵌套')
        # 输入工单名称
        WebDriverWait(self.driver,10,0.5).until(
            EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[1]/div/div/form/div[2]/div/input'))).send_keys('事件上报')
        # 点击处理
        WebDriverWait(self.driver,10,0.5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[8]/div/a[1]/span/i'))).click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        time.sleep(3)
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        time.sleep(3)
        #
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/form/div[1]/div[2]/div[1]/div/div/button[1]'))).click()
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/form/button[1]'))).click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        time.sleep(3)
        # 切入审批处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[11]/div[2]/iframe'))
        time.sleep(3)
        # 转应急小修/转专项小修/点击处理完成
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[1]/div/div/button[1]'))).click()
        # WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[1]/div/div/button[2]'))).click()
        # WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[1]/div/div/button[3]'))).click()

        # 切出嵌套
        self.driver.switch_to.default_content()
        a = WebDriverWait(self.driver, 10, 0.5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[1]/td/p'))).get_attribute("textContent")
        try:
            assert a == '处理完成'
            WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button'))).click()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
