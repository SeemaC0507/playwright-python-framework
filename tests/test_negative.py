from pages.login_page import LoginPage

def test_invalid_credentials(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("invalid_user", "wrongpassword")
    assert login_page.get_error_message() == "Epic sadface: Username and password do not match any user in this service"


def test_locked_user(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("locked_out_user", "secret_sauce")
    assert login_page.get_error_message() == "Epic sadface: Sorry, this user has been locked out."

def test_empty_fields(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("", "")
    assert login_page.get_error_message() == "Epic sadface: Username is required"   