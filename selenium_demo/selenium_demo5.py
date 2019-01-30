from selenium import webdriver

'''
cookies 获取、新增、删除
'''

# 定义浏览器位置
options = webdriver.ChromeOptions()
options.binary_location = 'D:\TSBrowser\TSBrowser.exe'

browser = webdriver.Chrome(options=options)
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())

browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
print(browser.get_cookies())

browser.delete_all_cookies()
print(browser.get_cookies())