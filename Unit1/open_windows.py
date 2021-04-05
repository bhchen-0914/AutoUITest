"""
窗口操作
"""
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.imooc.com")
driver.maximize_window()
#   登录
driver.find_element_by_id("js-signin-btn").click()
time.sleep(2)
driver.find_element_by_name("email").send_keys("18725730914")
driver.find_element_by_name("password").send_keys("cbh13647626691")
driver.find_element_by_class_name('moco-btn').click()
time.sleep(2)
#   移动指针位置
mouse = driver.find_elements_by_class_name('user-card-item')[1]
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(1)
#   进入个人设置
driver.find_elements_by_class_name("user-center-icon")[3].click()
time.sleep(2)
#   获取窗口列表
handle_list = driver.window_handles
#   获取当前窗口
current_handle = driver.current_window_handle
print(driver.window_handles)
#   切换窗口
for i in handle_list:
    if i != current_handle:
        driver.switch_to.window(i)
time.sleep(1)
driver.find_elements_by_class_name("inner-i-box")[1].find_element_by_class_name("moco-btn-normal").click()
handle_list = driver.window_handles
print(driver.window_handles)
driver.switch_to.window(handle_list[len(handle_list) - 1])
driver.maximize_window()
#   账号密码绑定微博
driver.find_element_by_id("jump_login_url_a").click()
handle_list = driver.window_handles
print(driver.window_handles)
driver.switch_to.window(handle_list[len(handle_list) - 1])
driver.find_element_by_name('username').send_keys("bhchen")
driver.find_element_by_name('password').send_keys("1234567")
time.sleep(3)
