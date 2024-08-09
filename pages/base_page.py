import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = os.getenv("base.url")

    def find_element(self, locator, time=30):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def wait_for_element_visibility(self, locator, timeout_in_seconds=30):
        try:
            WebDriverWait(self.driver, timeout_in_seconds).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def open(self, url):
        self.driver.get(url)
