from playwright.sync_api import Page

def test_open_saucedemo(page: Page):
    page.goto("https://www.saucedemo.com")
    assert "Swag Labs" in page.title()
    print("Page title is:", page.title())

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    assert "inventory" in page.url
    print("✅ Login successful! URL is:", page.url)
