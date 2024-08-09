import pytest

from api.repositories_api import RepositoriesAPI


@pytest.mark.skip
def test_get_repositories():
    api = RepositoriesAPI("https://api.github.com")
    response = api.get_repositories("your_username")
    assert response.status_code == 200
