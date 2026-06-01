import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, expected_error", [
    ("invalid_user", "wrongpassword", "do not match"),
    ("locked_out_user", "secret_sauce", "locked out"),
    ("", "", "Username is required"),
])
def test_login_scenarios(page, username, password, expected_error):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(username, password)
    assert expected_error in login_page.get_error_message()