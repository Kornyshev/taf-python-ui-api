import os

import pytest
from selenium import webdriver

from tests.models.user import User


@pytest.fixture
def driver():
    chrome = webdriver.Chrome()
    chrome.set_window_size(1920, 1080)
    yield chrome
    chrome.quit()


@pytest.fixture
def user():
    yield User(os.getenv("user.login"), os.getenv("user.password"))
