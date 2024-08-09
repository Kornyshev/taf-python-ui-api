from pages.login_page import LoginPage
from pages.main_page import MainPage


def test_successful_login(driver, user):
    login_page = LoginPage(driver)
    login_page.open("https://github.com/login")
    login_page.login_as(user)
    main_page = MainPage(driver)
    onboarding_notice_is_visible = main_page.wait_for_element_visibility(main_page.onboarding_notice)
    assert onboarding_notice_is_visible, "Onboarding notice should be visible"
    assert "GitHub" == driver.title


def test_unsuccessful_login(driver, user):
    login_page = LoginPage(driver)
    login_page.open("https://github.com/login")
    user.password = "incorrect_password"
    login_page.login_as(user)
    assert "Incorrect username or password." == login_page.get_incorrect_credentials_error_text()
