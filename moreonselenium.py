from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/xhtml')
search_field = driver.find_element_by_class_name('gLFyf')
search_field.send_keys('google')
search_field.submit()
driver.quit()