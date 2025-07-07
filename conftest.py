import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def page():
    """
    Фикстура Pytest для предоставления объекта Playwright Page.
    Запускает браузер перед каждым тестом и закрывает его после.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True) # headless=True для запуска без UI
        # browser = p.chromium.launch(headless=False) # headless=False для демонстрации UI
        page = browser.new_page()
        yield page
        browser.close()