from pages.base import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_field = self.page.get_by_label("Username")
        self.password_field = self.page.get_by_label("Password")
        self.submit_button = self.page.get_by_role("button", name="Submit")
        self.error_message = self.page.locator("#error")
        self.url = "https://practicetestautomation.com/practice-test-login/"

    def navigate(self):
        self.page.goto(self.url)

    def exceute_login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.submit_button.click()
    
    def get_error_message(self):
        return self.error_message.text_content()