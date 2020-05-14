# coding=utf-8
import time
from selenium.common.exceptions import NoSuchElementException
import os.path
from Base.logger import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


logger = Logger(logger="BasePage").getlog()


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver

    # 定位元素方法
    def find_element(self, selector):
        """
        :param selector:
        :return: element
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.visibility_of_element_located((By.ID, selector_value)))
            try:
                logger.info("find \' %s \' 成功 "
                            "by %s  value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()  # take screenshot
        elif selector_by == "n" or selector_by == 'name':
            element = WebDriverWait(self.driver, 10, 0.5).until(
                EC.visibility_of_element_located((By.NAME, selector_value)))
        elif selector_by == "c" or selector_by == 'class_name':
            element = WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.CLASS_NAME, selector_value)))
        elif selector_by == "l" or selector_by == 'link_text':
            element = WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,selector_value)))
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT,selector_value)))
        elif selector_by == "t" or selector_by == 'tag_name':
            element = WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.TAG_NAME,selector_value)))
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.XPATH,selector_value)))
                logger.info("find \' %s \' 成功 "
                            "by %s value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()
        elif selector_by == "s" or selector_by == 'selector_selector':
            element = WebDriverWait(self.driver, 10, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector_value)))
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    # 打开网址
    def get_url(self):
        self.get_url()

    # 退出浏览器
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        logger.info("浏览器前进.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        logger.info("浏览器后退.")

    # 刷新
    def refresh(self):
        self.driver.refresh()

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("隐式等待 %d 秒." % seconds)

    # 获取网页标题
    def get_page_title(self):
        logger.info("当前页面标题： %s" % self.driver.title)
        return self.driver.title

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭当前窗口.")
        except NameError as e:
            logger.error("关闭当前窗口失败 %s" % e)

    # 保存图片
    def get_windows_img(self):

        file_path = os.path.dirname(os.path.abspath('.')) + '\Test_resourse\Screenshots\\'
        rq = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("已获取截图并保存至路径 : \Screenshots")
        except NameError as e:
            logger.error("截图失败! %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector):
        el = self.find_element(selector)
        try:
            el.click()
            # logger.info("元素 \' %s \' 已点击." % el.text)
            logger.info("元素已点击")
        except NameError as e:
            logger.error("点击元素失败 %s" % e)

    # 输入
    def send_keys(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("已输入至 \' %s \' " % text)
        except NameError as e:
            logger.error("输入失败 %s" % e)
            self.get_windows_img()

    # 获取元素文案
    def get_text(self, selector):
        el = self.find_element(selector)
        try:
            return el.text
        except Exception as e:
            logger.error("未找到底层文案：%s" % e)
            self.get_windows_img()

    # switch to window
    def switch_to_window(self, title=None):
        handle = self.driver.current_window_handle
        if title:
            for handle_ in self.driver.window_handles:
                if handle != handle_:
                    self.driver.switch_to.window(handle)
                    if self.driver.title == title:
                        break
            else:
                raise ValueError("找不到标题为：" + title + "的页面")
        else:
            for handle_ in self.driver.window_handles:
                if handle != handle_:
                    self.driver.switch_to.window(handle)

    # 切换嵌套
    def switch_to_frame(self, selector=None):
        if selector:
            self.driver.switch_to.frame(self.find_element(selector))
            time.sleep(3)
        else:
            self.driver.switch_to.default_content()

    # 切出嵌套（防止上个方法错误临时使用）
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        time.sleep(3)

    # 鼠标hover元素
    def move_to_element(self, selector):
        ActionChains(self.driver).move_to_element(self.find_element(selector)).perform()

    # js
    def excute_script(self, js, *others):
        self.driver.excute_script(js, others)

    # 进度条
    def move_jindutiao(self, selector):
        self.driver.excute_script("arguments[0].scrollIntoView()",
                                  self.find_element(selector))

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logger.info("睡眠 %d 秒" % seconds)