"""
判断页面信息
根据title
"""
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://www.imooc.com")

# 返回title信息
title_name = driver.title
if "慕课网" in title_name:
    print("跳转正确")
else:
    print("网页不正确")

"""
EC.title_is 是一个类
实现了__call__方法，实例传入driver参数即可调用方法
    def __call__(self, driver):
        return self.title == driver.title
返回一个布尔值,当传入的title与driver的title完全一致时，返回true
"""
title_value = EC.title_is("慕课网")
print(title_value(driver))

"""
EC.title_contains 是一个类
实现了__call__方法，实例传入driver参数即可调用方法
    def __call__(self, driver):
        return self.title in driver.title
返回一个布尔值,当driver的title包含传入的title字段时，返回true
"""
title_value_contains = EC.title_contains("慕课网")
print(title_value_contains(driver))