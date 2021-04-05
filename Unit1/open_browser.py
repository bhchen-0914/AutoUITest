"""
打开浏览器
"""
import time
from selenium import webdriver

driver = ""


def open_browser(browser):
    # 将driver声明为全局变量，使浏览器打开后不会自动关闭
    global driver
    try:
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.firefox
        elif browser == "ie":
            driver = webdriver.Ie()
        elif browser == "edge":
            driver = webdriver.Edge()
        return driver
    except UnboundLocalError:
        print("browser does not exist！！")
        return None

def open_url(url, browser):
    web_driver = open_browser(browser)
    if web_driver:
        if url.startswith("http://"):
            web_driver.get(url)
        elif url.startswith("https://"):
            web_driver.get(url)
        else:
            web_driver.get("http://" + url)
    else:
        print("case error")


open_url("www.baidu.com", "chrome")
