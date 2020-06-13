from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.google.com/xhtml')
search_field = driver.find_elements_by_class_name('gLFyf')
for i in search_field:
    if i.tag_name == "input":
        i.send_keys('google', Keys.ARROW_LEFT, Keys.BACKSPACE, Keys.ENTER)
        break

