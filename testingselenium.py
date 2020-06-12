from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/xhtml')
time.sleep(5)
search_field = driver.find_element_by_name('q')
search_field.send_keys('google')
search_field.submit()
time.sleep(5)
driver.quit()
