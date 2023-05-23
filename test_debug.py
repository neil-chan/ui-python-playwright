from pages.checkbox import CheckboxPage
from playwright.sync_api import Page
import time


def test_debug(page: Page) -> None:
    checkbox_page = CheckboxPage(page)
    checkbox_page.navigate()
    checkbox_page.select_checkbox(1)
    time.sleep(10)
