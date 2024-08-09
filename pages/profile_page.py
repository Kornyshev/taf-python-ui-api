from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.mixins.navigation_mixin import NavigationMixin


class ProfilePage(BasePage, NavigationMixin):
    def __init__(self, driver):
        super().__init__(driver)
        self.yearly_contribution_section = (By.XPATH, "//div[contains(@class, 'yearly-contributions')]")
