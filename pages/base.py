from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    # def navigate_main(self):
    #     self.page.goto(self.base_url)

    # def click(self, locator):
    #     self.page.locator(locator).click()

    # def check(self, locator):
    #     self.page.locator(locator).check()

    # def uncheck(self, locator):
    #     self.page.locator(locator).uncheck()

    # def hover(self, locator):
    #     self.page.locator(locator).hover()

    # def navigate(self, url):
    #     self.page.goto(url)

    # def input(self, locator, text_input):
    #     self.page.locator(locator).fill(text_input)

    # def select_option(self, locator, option):
    #     self.page.locator(locator).select_option(option)
