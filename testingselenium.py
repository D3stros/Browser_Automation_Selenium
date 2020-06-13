from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedCondition
from selenium.webdriver.common.by import By

class has_css_class(object):
    def __init__(self, locator, css):
        self.locator = locator
        self.css = css

    def __call__(self, driver):
        element = driver.find_element(*self.locator)
        if self.css in element.get_attribute("class"):
            return element
        else:
            return False

driver = webdriver.Chrome()
driver.get('https://www.google.com/xhtml')

from selenium.webdriver import ActionChains
ac = ActionChains(driver)
driver.find_element_by_id('gb_70').click()
ac.click_and_hold(driver.find_element_by_class_name('snByac'))
ac.move_to_element(driver.find_element_by_name('identifier'))
ac.perform()


