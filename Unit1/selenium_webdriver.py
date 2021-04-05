"""
二次封装webdriver类
将常用操作封装进一个class中
常用操作包括：窗口最大化、最小化、刷新、设置窗口大小、前进、后退等
封装判断页面title方法
封装根据title切换页面的方法
"""
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

class selenium_driver:

    def __init__(self, browser):
        self.driver = self.get_driver(browser)

    def return_driver(self):
        return self.driver

    @staticmethod
    def get_driver(browser):
        """
         返回一个webdriver实例
         """
        try:
            if browser == "chrome":
                driver = webdriver.Chrome()
            elif browser == "firefox":
                driver = webdriver.firefox
            elif browser == "ie":
                driver = webdriver.Ie()
            elif browser == "edge":
                driver = webdriver.Edge()
            time.sleep(3)
            return driver
        except UnboundLocalError:
            print("browser does not exist！！")
            return None

    def open_url(self, url):
        """
        打开链接
        """
        if self.driver:
            if url.startswith("http://"):
                self.driver.get(url)
            elif url.startswith("https://"):
                self.driver.get(url)
            else:
                self.driver.get("http://" + url)
        else:
            print("case error")

    def handle_windows(self, *args):
        """
        常见窗口操作
        args:
        max:最大化
        min:最小化
        back:返回
        go:前进
        (x,y):设置窗口大小
        """

        command_list = ("max", "min", "back", "go")
        if len(args) == 0:
            raise Exception("参数不能为空")
        elif len(args) > 2:
            raise Exception("错误的参数个数")
        elif len(args) > 1:
            for param in args:
                if not isinstance(param, (int, float)):
                    raise Exception("请传入正确类型的参数(int, float)")
            self.driver.set_window_size(args[0], args[1])
        else:
            if args[0] not in command_list:
                raise Exception("错误的参数名(max,min,back,go)")
            if args[0] == "max":
                self.driver.maximize_window()
            elif args[0] == "min":
                self.driver.minimize_window()
            elif args[0] == "back":
                self.driver.back()
            else:
                self.driver.forward()

    #   判断页面title，如果正确返回true
    def _assert_title(self, title_value=None):
        if title_value is not None:
            title_obj = EC.title_contains(title_value)
            print(title_value + "验证结果：" + str(title_obj(self.driver)))
            return title_obj(self.driver)
        raise ValueError("请传入有效参数title_value")

    #   判断是否进入正确网页
    def open_url_is_true(self, url, title_value=None):
        self.open_url(url)
        return self._assert_title(title_value)

    #   切换窗口的方法
    def switch_windows(self, title_value=None):
        #   获取窗口列表
        handle_list = self.driver.window_handles
        print(handle_list)
        #   获取当前窗口
        current_window = self.driver.current_window_handle
        for window in handle_list:
            if window != current_window:
                time.sleep(1)
                #   先切换窗口，再判断
                self.driver.switch_to.window(window)
                if self._assert_title(title_value):
                    return
        #   若没找到相关窗口则回到当前窗口
        self.driver.switch_to.window(current_window)