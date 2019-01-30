import time
from selenium import webdriver

'''
模拟浏览器 前进、后退
'''

# 定义浏览器位置
options = webdriver.ChromeOptions()
options.binary_location = 'D:\TSBrowser\TSBrowser.exe'

browser = webdriver.Chrome(options=options)

browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')

# 后退
browser.back()

time.sleep(1)
# 前进
browser.forward()

browser.close()