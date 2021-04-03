
"""
打开浏览器
"""
import time

from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(5)
driver.close()