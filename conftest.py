import pytest
from playwright.sync_api import sync_playwright

BROWSER_CONFIGS = [
    {"name": "chromium_headless", "browser_type": "chromium", "headless": True},
    {"name": "firefox_headless", "browser_type": "firefox", "headless": True},
    {"name": "webkit_headless", "browser_type": "webkit", "headless": True},
    # Example: Headed modes
    # {"name": "chromium_headed", "browser_type": "chromium", "headless": False, "slow_mo": 500},
]

@pytest.fixture(scope="session", params=BROWSER_CONFIGS, ids=[c["name"] for c in BROWSER_CONFIGS])
def browser_config(request):
    """
    Pytest fixture to parametrize browser configurations.
    """
    return request.param

@pytest.fixture(scope="session")
def browser(browser_config):
    """
    Pytest fixture to launch a browser based on the browser_config.
    """
    with sync_playwright() as p:
        browser_type = browser_config["browser_type"]
        launch_options = {k: v for k, v in browser_config.items() if k not in ["name", "browser_type"]}

        if browser_type == "chromium":
            browser_instance = p.chromium.launch(**launch_options)
        elif browser_type == "firefox":
            browser_instance = p.firefox.launch(**launch_options)
        elif browser_type == "webkit":
            browser_instance = p.webkit.launch(**launch_options)
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")

        yield browser_instance
        browser_instance.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()