import pytest

from pages.repositories_page import RepositoriesPage

@pytest.mark.skip
def test_repositories(driver):
    repo_page = RepositoriesPage(driver)
    repo_page.open("https://github.com/your_username?tab=repositories")
    repos = repo_page.get_repositories()
    assert "your_repository" in repos
