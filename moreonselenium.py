from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.google.com/xhtml')
driver.get('https://www.youtube.com')
driver.back()
driver.forward()


