from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.elements.repository_element import RepositoryElement
from pages.mixins.navigation_mixin import NavigationMixin


class RepositoriesPage(BasePage, NavigationMixin):
    def __init__(self, driver):
        super().__init__(driver)
        self.repo_list_locator = (By.CSS_SELECTOR, "div#user-repositories-list li")

    def get_repository_elements(self):
        repo_elements = self.driver.find_elements(*self.repo_list_locator)
        return [RepositoryElement(self.driver, repo) for repo in repo_elements]

    def get_all_visible_titles(self):
        repository_elements = self.get_repository_elements()
        return [repo.get_title() for repo in repository_elements]
