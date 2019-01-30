from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


options = webdriver.ChromeOptions()
#options.binary_location = r"E:\python\install\Scripts\chromedriver.exe"
options.binary_location = r"D:\TSBrowser\TSBrowser.exe"

browser = webdriver.Chrome(options=options)
try:
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 30)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))

    print(browser.current_url)
    print(browser.get_cookies())
    #print(browser.page_source)
finally:
    # 浏览器关闭
    browser.close()