from pages.login_page import LoginPage

def test_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_logged_in() == True

def test_something(logged_in_page):
    assert "inventory" in logged_in_page.url