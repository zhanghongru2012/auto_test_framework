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

        # 点击养护管理
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[3]/div/span[3]"))).click()
        # 点击应急小修
        WebDriverWait(self.driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[3]/ul/li[2]/div/span[2]"))).click()
        # 切入主嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/iframe"))
        time.sleep(3)
        # 点击小修类型下拉
        try:
            self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[2]/input[1]").click()
        except Exception as e:
            print(e)
            self.driver.find_element_by_xpath(
                "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[2]/input[1]").click()
        
        # 选择路产损坏
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[2]/span").click()
        # 点击管理单位下拉
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[3]/div/div[2]/input[1]").click()
        # 选择禹城公路局
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div/ul/li/div/span[2]").click()
        # 输入工程名称
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[4]/div[2]/input").send_keys("工程名称")
        # 点击负责单位
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[6]/div[2]/input").click()
        # 切出主嵌套
        self.driver.switch_to.default_content()
        time.sleep(3)
        # 切入单位选择嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[11]/div[2]/iframe"))
        time.sleep(3)
        # 切出嵌套
        self.driver.switch_to.default_content()
        time.sleep(3)
        # 点击上个嵌套页面里面非嵌套的最大化
        self.driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]/i").click()
        time.sleep(3)
        # 切入选择单位嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[11]/div[2]/iframe"))
        time.sleep(3)
        # 点击选择单位- 禹城公路站
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div/div[1]/label/span").click()
        # 点击确定按钮
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/button").click()
        # 切出选择单位嵌套
        self.driver.switch_to.default_content()
        time.sleep(3)
        # 切入主嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/iframe"))
        # 点击项目负责人下拉
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[7]/div/div[2]/input[1]").click()
        # 选择禹城测试
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[12]/span").click()
        # 输入项目负责人电话
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[8]/div[2]/input").send_keys("18510684958")
        # 点击选择派工时间
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[9]/div[2]/input[1]").click()
        # 直接点击选择时间按钮
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div[2]/div[3]/a[2]/span").click()
        # 输入维修原因
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[10]/div[2]/textarea").send_keys("维修原因")
        # 输入工程内容
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[11]/div[2]/textarea").send_keys("工程内容")
        # 输入处理要求
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[12]/div[2]/textarea").send_keys("处理要求")
        # 单位类型下拉
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/input[1]").click()
        # 选择单位类型 - 公路站
        self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[3]/span").click()
        # 切换到事件信息tab
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[1]/div[1]/div[1]/ul/li[2]/span").click()
        # --------------事件信息操作-------------
        # 点击事件细类下拉
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div[2]/input[1]").click()
        # 选择路基
        try:
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span").click()
        except Exception as e:
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span").click()
        # 选择巡查中队
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[2]/div[5]/div/div[2]/input[1]").click()
        # 选择一中队
        try:
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[4]/span").click()
        except Exception as e:
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[4]/span").click()

        # 选择上报人员下拉
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[2]/div[7]/div/div[2]/input[1]").click()
        # 选择禹城一中队
        WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div/div[1]/div[1]/div/div/div[12]/span"))).click()
        # 事件描述输入
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[2]/div[8]/div[2]/textarea").send_keys(
            "事件描述")
        # 应急措施输入
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[2]/div[9]/div[2]/textarea").send_keys(
            "应急措施")
        # 维修建议输入
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div[2]/div[10]/div[2]/textarea").send_keys(
            "维修建议")
        # 所在路线下拉
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/input[1]").click()
        # 选择济南-德州
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]"))).click()
        # 选择上下行
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/input[1]").click()
        time.sleep(3)
        # 选择上行
        try:
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span").click()
        except Exception as e:
            print(e)
            self.driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span").click()

        # 输入起点桩号
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[3]/div[2]/input").send_keys(
            "52.522")
        # 输入止点桩号
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[4]/div[2]/input").send_keys(
            "66.22")
        # 输入偏移量
        self.driver.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div[5]/div[2]/input").send_keys(
            "0.07")
        # 上传图片
        up_load = WebDriverWait(self.driver, 5, 0.5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[3]/div[2]/div/div/div[3]/div/div[2]/input')))
        up_load.send_keys("E:\\aaa\\a.jpg")
        time.sleep(5)
        # 开始上传
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div/form/div/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/div/div/div/div[1]/div/div[3]/div[2]/div/div/div[1]/div/div[2]').click()
        self.driver.switch_to.default_content()
        time.sleep(3)
        # 点击知道了
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button").click()
        # 切入主嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/iframe"))
        # 点击保存按钮
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div/div/div[1]/button[2]").click()

        # 切出主嵌套
        self.driver.switch_to.default_content()
        # 找到保存后提示信息
        displayed_or = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[1]").is_displayed()
        a = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div[2]/div[1]/div/table/tr[1]").get_attribute('textContent')
        print("元素被隐藏判断: false为隐藏, True为非隐藏:\n", displayed_or)
        try:
            assert a == "保存成功"
        except:
            print("信息填写不完整")



        print("""
               \033[1;30;45m--------------------彩    蛋--------------------\033[0m
               \033[1;30;45m|                                             |\033[0m
               \033[1;30;45m|                                             |\033[0m
               \033[1;30;45m|                  !success!                  |\033[0m
               \033[1;30;45m|                                             |\033[0m
               \033[1;30;45m|                                             |\033[0m
               \033[1;30;45m--------------------  end  --------------------\033[0m
               """)

        # 首页用户信息-鼠标悬停
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('user-info')).perform()
        # 工单管理-点击
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[3]/div/div[2]/ul/li[6]/span[2]'))).click()
        print('打开流程管理frame')
        # 最大化流程管理嵌套框
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]'))).click()
        time.sleep(3)
        # ----处理应急事件----
        # 切入流程管理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[11]/div[2]/iframe'))
        time.sleep(3)
        print('已切入流程管理嵌套')
        # 输入工单名称
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/form/div[2]/div/input'))).send_keys('应急事件上报')
        # 点击处理
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[8]/div/a[1]/span/i'))).click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        time.sleep(3)
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        time.sleep(3)
        # 选择预案-点击
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/button[1]').click()
        # 切入应急预案嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[11]/div[2]/iframe'))
        time.sleep(3)
        # 选择第一个应急预案
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[1]/label/span').click()
        # 点击选中
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/button[2]').click()
        # 切出应急预案嵌套
        self.driver.switch_to.default_content()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        time.sleep(3)
        # 输入启动人
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/form/div/div/div[1]/div/div[1]/div[2]/div[7]/div[2]/input').send_keys('启动人1')
        # 选择启动方式
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/form/div/div/div[1]/div/div[1]/div[2]/div[8]/div/div[2]/input[1]').click()
        # 启动方式选择'书面打印'
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span').click()
        # 点击保存
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/button[1]').click()
        # 点击启动
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/button[3]').click()
        # 点击传递
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/button[2]').click()
        # 切出任务处理嵌套
        self.driver.switch_to.default_content()
        # 确认传递
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]').click()

        # ----反馈处理结果----
        # 切入工单管理嵌套
        self.driver.switch_to.frame('/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]')
        # 搜索任务名称'反馈处理结果'
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/form/div[3]/div/input').send_keys('反馈处理结果')
        # 点击处理
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[8]/div/a[1]/span/i'))).click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 输入结束人
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/form/div/div/div[1]/div/div[1]/div[2]/div[7]/div[2]/input').send_keys('结束人')
        # 选择结束方式
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/form/div/div/div[1]/div/div[1]/div[2]/div[8]/div/div[2]/input[1]').click()
        # 结束方式选择'书面结束'
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span').click()
        # 选择是否结束
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div/div/div/div[1]/div/div/form/div/div/div[1]/div/div[1]/div[2]/div[9]/div/div[2]/input[1]').click()
        # 选择'是'
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div[1]/div/div/div[1]/span').click()
        # 点击'保存'
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/button[1]').click()
        # 切出任务处理嵌套
        self.driver.switch_to.default_content()
        # 点击知道了
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击传递
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/button[2]').click()
        # 切出任务处理嵌套
        self.driver.switch_to.default_content()
        # 点击确认传递
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]').click()

        # ----生成应急处置报告----
        # 切入工单管理嵌套
        self.driver.switch_to.frame('/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]')
        # 搜索任务名称'生成应急处置报告'
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/form/div[3]/div/input').send_keys('生成应急处置报告')
        # 点击处理
        WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[8]/div/a[1]/span/i'))).click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 切出任务处理嵌套
        self.driver.switch_to.default_content()
        # 点击最大化
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div[11]/div[1]/table/tr/td[2]/div/div/div/a[2]').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 输入波及范围
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/form/div/div/div[1]/div[2]/input').send_keys('波及范围')
        # 输入伤亡情况
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/form/div/div/div[2]/div[2]/input').send_keys('伤亡情况')
        # 输入人员投入情况
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/form/div/div/div[3]/div[2]/textarea').send_keys('人员投入情况')
        # 输入设备投入情况
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/form/div/div/div[4]/div[2]/textarea').send_keys('设备投入情况')
        # 输入物资投入情况
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/form/div/div/div[5]/div[2]/textarea').send_keys('物资投入情况')
        # 输入遇到的问题
        self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div/div/div/div[1]/div/div/form/div/div/div[6]/div[2]/textarea').send_keys('遇到的问题')
        # 点击保存
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[1]/div/div/button[1]').click()
        # 切出嵌套
        self.driver.switch_to.default_content()
        # 点击知道了
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button').click()
        # 切入任务处理嵌套
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[11]/div[2]/iframe'))
        # 点击生成应急处置报告
        self.driver.find_element_by_xpath('/html/body/div[2]/button').click()
        # 键盘esc
        ActionChains(self.driver).send_keys(Keys.ESCAPE)
        # 点击传递
        self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[1]/div/div/button[2]').click()
        # 切出任务处理嵌套
        self.driver.switch_to.default_content()
        # 点击确认传递
        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div/table/tr[2]/td/button[1]').click()
        # 切出嵌套
        # self.driver.switch_to.default_content()
        # 键盘esc
        # ActionChains(self.driver).send_keys(Keys.ESCAPE)
        # ----- 至此 结束 -----


if __name__ == '__main__':
    unittest.main()
