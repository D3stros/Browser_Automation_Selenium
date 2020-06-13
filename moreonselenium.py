from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.google.com/xhtml')
cookie = {'name': 'token', 'value': '4asdasdasdasddas'}
driver.add_cookie(cookie)
driver.get('https://www.google.com')
print(driver.get_cookie('token'))
print(driver.get_cookies())




