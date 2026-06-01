class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username_field = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def goto(self):
        self.page.goto("https://www.saucedemo.com")
        

    def login(self, username, password):
        self.username_field.fill(username)
        self.password.fill(password)
        self.login_button.click()
        

    def is_logged_in(self):
        return "inventory" in self.page.url

    def get_error_message(self):
        return self.page.locator("[data-test='error']").text_content()    
  

