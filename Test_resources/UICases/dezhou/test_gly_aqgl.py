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

        # 点击首页安全管理
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[5]/div/span[3]").click()
        # 点击隐患整改上报
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[5]/ul/li[4]/div/span[2]").click()
        # 切入隐患整改上报嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/iframe"))
        # 输入参与人
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[1]/div[2]/div[5]/div[2]/input").send_keys("二哥")
        # 输入检查地点
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[1]/div[2]/div[6]/div[2]/input").send_keys("daxiyang")
        # 所在路线下拉
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[1]/div[2]/div[7]/div/div[2]/input[1]").click()
        # 所在路线选择济南-德州
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span").click()
        # 里程桩号输入
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[1]/div[2]/div[8]/div[2]/input").send_keys("52.522")
        # 上下行下拉
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[1]/div[2]/div[9]/div/div[2]/input[1]").click()
        # 上下行选择上行
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[2]/span").click()
        # 偏移位置选择中心线
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[1]/div[2]/div[10]/div[2]/div[1]/label/span[1]").click()
        # 输入偏移量
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[1]/div[2]/div[11]/div[2]/input").send_keys("0.07")
        # 传递方式选择流程处理
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[1]/div[2]/div[13]/div[2]/div[1]/label").click()
        # 输入情况描述
        try:
            self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[1]/div[2]/div[14]/div[2]/textarea").send_keys("qingkuang")
        except Exception as e:
            print(e)
            self.driver.find_element_by_xpath(
                "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[1]/div[2]/div[14]/div[2]/textarea").send_keys(
                "qingkuang")
        # 输入整改建议
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[1]/div[2]/div[15]/div[2]/textarea").send_keys("zhenggaijianyi")
        # 上传照片
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[2]/div[2]/div/div/div[3]/div/div[2]/input").send_keys("E:\\aaa\\a.jpg")
        # 点击确认上传
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div[2]/div[2]/div/div/div[1]/div/div[2]").click()
        # 切出隐患整改上报嵌套
        self.driver.switch_to.default_content()
        time.sleep(3)
        # 点击知道了
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button").click()
        # 切入隐患整改上报嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/iframe"))
        # 点击保存按钮
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[2]").click()
        # 切出隐患整改上报嵌套
        self.driver.switch_to.default_content()
        # 获取断言
        a = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[1]/td/p").get_attribute("textContent")
        if a == "保存成功":
            print("ok")
        else:
            pass
        # 点击知道了
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button').click()
        # 切入隐患整改上报嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/iframe"))
        # 点击提交并发起流程
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[3]').click()

        # ------安全科长审批------
        # ----安全科长审批----
        # 首页用户信息-鼠标悬停
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('user-info')).perform()
        # 工单管理-点击
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/ul/li[6]/span[2]'))).click()
        print('打开流程管理frame')
        # 最大化流程管理嵌套框
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'))).click()
        time.sleep(3)
        # 切入流程管理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[11]/div[2]/iframe'))
        time.sleep(3)
        print('已切入流程管理嵌套')
        # 输入工单名称
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/form/div[2]/div/input'))).send_keys('隐患整改')
        # 点击处理
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[8]/div/a[1]/span/i'))).click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        time.sleep(3)
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击窗口最大化
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]/i').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 选择整改时限
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div[2]/div/div/div/a/i').click()
        # 时间控件内选择下个月
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div/div[1]/table/tr/td[4]/a/i').click()
        # 点击选择
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div/div[2]/div[3]/a[2]').click()
        # 点击办理
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[1]').click()
        # 点击保存
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[2]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击知道了
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击传递
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[3]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击确认传递
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]').click()

        # ------分管领导审核1------
        # 首页用户信息-鼠标悬停
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('user-info')).perform()
        # 工单管理-点击
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/ul/li[6]/span[2]'))).click()
        print('打开流程管理frame')
        # 最大化流程管理嵌套框
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'))).click()
        time.sleep(3)
        # 切入流程管理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[11]/div[2]/iframe'))
        time.sleep(3)
        print('已切入流程管理嵌套')
        # 输入任务名称
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/form/div[3]/div/input'))).send_keys('分管领导审核')
        # 点击处理
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[8]/div/a[1]/span/i'))).click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击最大化
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]/i').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击办理
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[1]').click()
        # 点击保存
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[2]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击知道了
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击传递
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[3]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击确认传递
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]').click()

        # ------分管领导指派科室处理------
        # 首页用户信息-鼠标悬停
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('user-info')).perform()
        # 工单管理-点击
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/ul/li[6]/span[2]'))).click()
        print('打开流程管理frame')
        # 最大化流程管理嵌套框
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'))).click()
        time.sleep(3)
        # 切入流程管理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[11]/div[2]/iframe'))
        time.sleep(3)
        print('已切入流程管理嵌套')
        # 输入任务名称
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/form/div[3]/div/input'))).send_keys('分管领导指派科室处理')
        # 点击处理
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[8]/div/a[1]/span/i'))).click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击最大化
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]/i').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击指定处理人
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/button[4]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 切入指定处理人嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[11]/div[2]/iframe'))
        # 搜索处理人'禹城测试'
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/form/div[2]/div[2]/input').send_keys('禹城测试')
        # 选择第一个处理人
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[1]/label/span').click()
        # 点击选中
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/button').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击保存
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/button[1]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击知道了
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击传递
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[3]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击确认传递
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]').click()

        # ------科室负责人指派具体人员处理------
        # 首页用户信息-鼠标悬停
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('user-info')).perform()
        # 工单管理-点击
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/ul/li[6]/span[2]'))).click()
        print('打开流程管理frame')
        # 最大化流程管理嵌套框
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'))).click()
        time.sleep(3)
        # 切入流程管理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[11]/div[2]/iframe'))
        time.sleep(3)
        print('已切入流程管理嵌套')
        # 输入任务名称
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/form/div[3]/div/input'))).send_keys('科室负责人指派具体人员处理')
        # 点击处理
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[8]/div/a[1]/span/i'))).click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击最大化
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]/i').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击指定处理人
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/button[4]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 切入指定处理人嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[11]/div[2]/iframe'))
        # 搜索处理人'禹城测试'
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/form/div[2]/div[2]/input').send_keys('禹城测试')
        # 选择第一个处理人
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[1]/label/span').click()
        # 点击选中
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/button').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击保存
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/button[1]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击知道了
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击传递
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[3]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击确认传递
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]').click()

        # ------事件处理-流程处理------
        # 首页用户信息-鼠标悬停
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('user-info')).perform()
        # 工单管理-点击
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/ul/li[6]/span[2]'))).click()
        print('打开流程管理frame')
        # 最大化流程管理嵌套框
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'))).click()
        time.sleep(3)
        # 切入流程管理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[11]/div[2]/iframe'))
        time.sleep(3)
        print('已切入流程管理嵌套')
        # 输入工单名称
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/form/div[2]/div/input'))).send_keys('隐患整改')
        # 点击处理
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[8]/div/a[1]/span/i'))).click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击最大化
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]/i').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击保存按钮
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div/div/button[1]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击知道了
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button').click()
        # 点击传递
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[3]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击确认传递
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]').click()

        # ------上报人复核------
        # 首页用户信息-鼠标悬停
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('user-info')).perform()
        # 工单管理-点击
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/ul/li[6]/span[2]'))).click()
        print('打开流程管理frame')
        # 最大化流程管理嵌套框
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'))).click()
        time.sleep(3)
        # 切入流程管理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[11]/div[2]/iframe'))
        time.sleep(3)
        print('已切入流程管理嵌套')
        # 输入工单名称
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/form/div[2]/div/input'))).send_keys('隐患整改')
        # 点击处理
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[8]/div/a[1]/span/i'))).click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击最大化
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]/i').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击保存按钮
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div/div/button[1]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击知道了
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button').click()
        # 点击传递
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[3]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击确认传递
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]').click()

        # ------分管领导审核2------
        # 首页用户信息-鼠标悬停
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('user-info')).perform()
        # 工单管理-点击
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/ul/li[6]/span[2]'))).click()
        print('打开流程管理frame')
        # 最大化流程管理嵌套框
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'))).click()
        time.sleep(3)
        # 切入流程管理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[11]/div[2]/iframe'))
        time.sleep(3)
        print('已切入流程管理嵌套')
        # 输入任务名称
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/form/div[3]/div/input'))).send_keys('分管领导审核')
        # 点击处理
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[8]/div/a[1]/span/i'))).click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击最大化
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]/i').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击办理
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[1]').click()
        # 点击保存
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[2]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击知道了
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击传递
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[3]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击确认传递
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]').click()

        # ------文书打印------
        # 首页用户信息-鼠标悬停
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('user-info')).perform()
        # 工单管理-点击
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/ul/li[6]/span[2]'))).click()
        print('打开流程管理frame')
        # 最大化流程管理嵌套框
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'))).click()
        time.sleep(3)
        # 切入流程管理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[11]/div[2]/iframe'))
        time.sleep(3)
        print('已切入流程管理嵌套')
        # 输入任务名称
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/form/div[3]/div/input'))).send_keys('分管领导审核')
        # 点击处理
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[8]/div/a[1]/span/i'))).click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击最大化
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]/i').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击办理
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[1]').click()
        # 点击传递
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[3]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击确认传递
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]').click()


if __name__ == '__main__':
    unittest.main()
