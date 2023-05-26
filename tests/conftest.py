import os
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='session')
def page():
    with sync_playwright() as playwright:
        if os.getenv('DOCKER_RUN'):  
            browser = playwright.chromium.launch(headless=True, args=['--no-sandbox'])
        else:
            browser = playwright.chromium.launch(headless=False)
        
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
