import pytest

from api.users_api import UsersAPI


@pytest.mark.skip
def test_get_user():
    api = UsersAPI("https://api.github.com")
    response = api.get_user("your_username")
    assert response.status_code == 200
