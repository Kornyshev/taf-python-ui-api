from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class NavigationMixin:
    def __init__(self, driver):
        self.driver = driver
        self.navigation_toggle = (By.CSS_SELECTOR, "button[aria-label='Open user navigation menu']")
        self.profile_link = (By.XPATH, "//span[text()='Your profile']")
        self.repositories_link = (By.XPATH, "//span[text()='Your repositories']")
        self.close_icon = (By.XPATH, "//div[@role='dialog']//button[@aria-label='Close']")

    def open_navigation_panel(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.navigation_toggle)).click()

    def go_to_profile(self):
        self.open_navigation_panel()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.profile_link)).click()

    def go_to_repositories(self):
        self.open_navigation_panel()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.repositories_link)).click()

    def close_navigation_panel(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.close_icon)).click()
