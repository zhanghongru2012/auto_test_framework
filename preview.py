# import os
#
# dir = os.path.dirname(os.path.abspath('.'))
# chrome_driver_path = dir + '\Tools\chromedriver.exe'
# print(dir)
# print(chrome_driver_path)

from selenium import webdriver
import time
chrome_driver = r"C:\Users\Administrator\Documents\time_manage\UITestFramework\Test_resourse\Tools\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get('http://www.changhe-wl.com/')
time.sleep(3)
print(driver.title)
# driver.find_element_by_xpath('//*[@id="index1"]/div[2]/ul/li[1]').click()
try:
    driver.find_element_by_class_name('exponent-bot-img').click()
except Exception as e:
    print(e)


q = driver.current_window_handle
print(q)
time.sleep(3)
driver.quit()
