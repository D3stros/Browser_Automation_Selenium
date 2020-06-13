from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedCondition
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.google.com/xhtml')
try:
    element = WebDriverWait(driver, 5).until(
        ExpectedCondition.presence_of_element_located((By.NAME, "quh"))
    )
    element.send_keys("google")
finally:
    driver.quit()

