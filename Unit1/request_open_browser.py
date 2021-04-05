"""
根据selenium底层打开浏览器原理
封装打开浏览器方法
"""

import requests
import json
import time
import os


class OpenBrowser:

    def __init__(self, browserName):
        #   前置操作：启动jar包服务
        self.start_selenium_standalone(self.get_shell_command())
        self.browserName = browserName
        self.url = "http://127.0.0.1:8899/wd/hub/session/"
        self.driver = self.get_driver()

    #  返回drivers,实质上使包含session尾部信息的url
    def get_driver(self):
        params = {
            'desiredCapabilities': {
                'browserName': self.browserName
            }
        }
        json_param = json.dumps(params)
        session = requests.post(self.url, json_param).json()["sessionId"]
        driver = self.url + session
        return driver

    #   拼接shell命令
    @staticmethod
    def get_shell_command():
        curPath = os.path.abspath(os.path.dirname(__file__))
        # 获取项目根目录
        rootPath = curPath[:curPath.find("AutoUITest\\") + len("AutoUITest\\")]
        startup = "java -jar" + " " + rootPath + "\\selenium-server-standalone-4.0.0-alpha-1.jar -port 8899"
        return startup

    #  执行shell命令，设置主线程延时
    @staticmethod
    def start_selenium_standalone(command):
        # os.system会阻塞当前进程，需加入start 语句在阻塞后调起进程
        os.system("start " + command)
        time.sleep(3)

    #   使用post携带json格式信息访问目标地址
    def open_url(self, url):
        base_url = self.driver + '/url'
        if url.startswith("http://"):
            data = {
                "url": url
            }
        elif url.startswith("https://"):
            data = {
                "url": url
            }
        else:
            data = {
                "url": "https://" + url
            }
        requests.post(base_url, json.dumps(data))


if __name__ == '__main__':
    ob = OpenBrowser('internet explorer')
    ob.open_url("www.baidu.com")
