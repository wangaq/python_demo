import time
from selenium import webdriver
'''
浏览器窗口之间跳转

'''

# 定义浏览器位置
options = webdriver.ChromeOptions()
options.binary_location = 'D:\TSBrowser\TSBrowser.exe'

browser = webdriver.Chrome(options=options)
browser.get('https://www.baidu.com')

browser.execute_script('window.open()')
#print(browser.window_handles)

browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')

time.sleep(5)

browser.switch_to.window(browser.window_handles[0])
browser.get('https://python.org')