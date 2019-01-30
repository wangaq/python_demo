from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 定义浏览器位置
options = webdriver.ChromeOptions()
options.binary_location = 'D:\TSBrowser\TSBrowser.exe'

# 启动浏览器
browser = webdriver.Chrome(options=options)
browser.get('https://www.taobao.com')

# 获取输入框
input = browser.find_element(By.ID,'q')

# 填写查询字段
input.send_keys('iPhone')

time.sleep(3)

# 清空输入框
input.clear()

# 再次填写查询字段
input.send_keys('iPad')

# 获取查询按钮、点击查询
button = browser.find_element_by_class_name('btn-search')
button.click()

# 完美！！