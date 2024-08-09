from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.mixins.navigation_mixin import NavigationMixin


class MainPage(BasePage, NavigationMixin):
    def __init__(self, driver):
        super().__init__(driver)
        self.onboarding_notice = (By.CSS_SELECTOR, "div.new-feed-onboarding-notice")
        self.start_repository_section = (By.CSS_SELECTOR, "section[aria-label='Start a new repository']")
        self.latest_changes = (By.CSS_SELECTOR, "div.dashboard-changelog")
