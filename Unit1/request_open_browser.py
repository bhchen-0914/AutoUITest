"""
根据selenium底层打开浏览器原理
封装打开浏览器方法
"""

import requests
import json
import time
import os


class OpenBrowser:

    def __init__(self):
        self.params = {
            'desiredCapabilities': {
                'browserName': 'chrome'
            }
        }
        self.url = "http://127.0.0.1:8899/wd/hub/session/"

        self.curPath = os.path.abspath(os.path.dirname(__file__))

    def get_shell_command(self):
        # 获取项目根目录
        rootPath = self.curPath[:self.curPath.find("AutoUITest\\") + len("AutoUITest\\")]
        startup = "java -jar" + " " + rootPath + "\\selenium-server-standalone-4.0.0-alpha-1.jar -port 8899"
        return startup

    @staticmethod
    def start_selenium_standalone(command):
        # os.system会阻塞当前进程，需加入start 语句在阻塞后调起进程
        os.system("start "+command)
        time.sleep(5)

    def start_browser(self):
        json_param = json.dumps(self.params)
        response = requests.post(self.url, json_param)
        print(response.json())

    def run(self):
        command = self.get_shell_command()
        self.start_selenium_standalone(command)
        self.start_browser()


if __name__ == '__main__':
    ob = OpenBrowser()
    ob.run()

