from selenium import webdriver
from selenium.webdriver.common.by import By

'''
获取返回数据节点
'''
options = webdriver.ChromeOptions()
options.binary_location = 'D:\TSBrowser\TSBrowser.exe'

browser = webdriver.Chrome(options=options)
browser.get('https://www.taobao.com')

#print(browser.page_source)

input_first = browser.find_element(By.ID, 'q')
print(input_first)


browser.close()
