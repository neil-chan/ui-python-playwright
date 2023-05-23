from pages.checkbox import CheckboxPage
from pages.login import LoginPage
from playwright.sync_api import expect


class TestDebug:
    def test_login_incorrect_username(self, page):
        login_page = LoginPage(page)
        login_page.navigate()
        login_page.execute_login("wrong", "username")
        expect(login_page.error_message).to_have_text("Your username is invalid!")

    def test_selecting_checkbox(self, page):
        checkbox_page = CheckboxPage(page)
        checkbox_page.navigate()
        checkbox_page.select_checkbox(2)
        locator = page.get_by_role("checkbox").nth(1)
        expect(locator).to_be_checked()
