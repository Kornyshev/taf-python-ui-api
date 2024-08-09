import re

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.models.user import User


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_field = (By.CSS_SELECTOR, "input[name='login']")
        self.password_field = (By.CSS_SELECTOR, "input[name='password']")
        self.submit_button = (By.CSS_SELECTOR, "input[type='submit']")
        self.incorrect_credentials_error = (By.CSS_SELECTOR, "div.flash-error div div")

    def login_as(self, user: User):
        self.find_element(self.login_field).send_keys(user.username)
        self.find_element(self.password_field).send_keys(user.password)
        self.find_element(self.submit_button).click()

    def get_incorrect_credentials_error_text(self):
        super().wait_for_element_visibility(self.incorrect_credentials_error, 30)
        error_element = self.find_element(self.incorrect_credentials_error)
        return error_element.text.strip()
