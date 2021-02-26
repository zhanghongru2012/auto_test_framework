from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
import time


dir = os.path.abspath('.') + '\\Test_resources'
# 当前版本：86.0.4044.198
chrome_driver_path = dir + '\\Tools\\chromedriver.exe'
print(chrome_driver_path)
driver = webdriver.Chrome()

driver.get('http://192.168.0.50:7082/security/entry-ctl/login')
driver.maximize_window()
driver.find_element_by_id('user').send_keys('admin')
driver.find_element_by_id('pwd').send_keys('123456')
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/form/div[3]/button').click()

driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/div/div/ul/li/ul/li[5]/div/span[2]'
).click()
time.sleep(5)

frame_goods_manager = '/html/body/div[2]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/iframe'
driver.switch_to.frame(driver.find_element_by_xpath(frame_goods_manager))

scrollbar = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[2]/div')
scrollbar_area = driver.find_element_by_xpath(
    '/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]')

js_code_scrollbar = "arguments[0].style.setProperty('transform','translate3d(919.304px, 0px, 0px)');"
js_code_scrollbar_area = "arguments[0].style.setProperty('transform','translate3d(-2006px, 0px, 0px)');"
driver.execute_script(js_code_scrollbar, scrollbar)
driver.execute_script(js_code_scrollbar_area, scrollbar_area)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/div[2]/div/div/div/div[1]/div/div[1]/div[28]/div/div/label[1]').click()




