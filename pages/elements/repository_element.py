from selenium.webdriver.common.by import By


class RepositoryElement:
    def __init__(self, driver, root):
        self.driver = driver
        self.root = root
        self.title_locator = (By.CSS_SELECTOR, "h3 a")
        self.repo_type_locator = (By.CSS_SELECTOR, "h3 span.Label")
        self.updated_date_locator = (By.XPATH, "//relative-time/..")

    def get_title(self):
        return self.root.find_element(*self.title_locator).text.strip()

    def get_repo_type(self):
        return self.root.find_element(*self.repo_type_locator).text.strip()

    def get_updated_date(self):
        return self.root.find_element(*self.updated_date_locator).text.strip()
