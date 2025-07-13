import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

VALID_USER = "NicePotatoSalad"
INVALID_USER = "InvalidUser12345SUPERINVALIDNOONEWILLEVERTAKETHISNAMEQWERTY"
INVALID_PASSWORD = "12345Salad"
EMPTY_STRING = ""

# --- UI tests ---

def test_main_header_displayed_correctly(page, text="Sign in to GitHub"):
    login_page = LoginPage(page)
    login_page.navigate()

    assert login_page.main_header.is_visible(), "Main header is not visible"
    assert login_page.get_main_header_text() == text, \
        f"Main header text is expected to be {text}, but got {login_page.get_main_header_text}"
    
def test_login_input_field_displayed_correctly(page):
    login_page = LoginPage(page)
    login_page.navigate()

    assert login_page.login_input_field.is_visible(), "Login input field is not visible"

def test_login_input_field_attributes_correct(page):
    # Check type, name, autocapitalize, autocorrect, autocomplete, autofocus, required
    login_page = LoginPage(page)
    login_page.navigate()

    expected_attributes = {
        "type": "text",
        "name": "login",
        "autocapitalize": ["off", "none"], # Expect either "off" or "none"
        "autocorrect": "off",
        "autocomplete": "username",
        "autofocus": "autofocus",
        "required": "required"
    }

    for attribute_name, expected_value in expected_attributes.items():
        actual_value = login_page.get_login_input_attribute(attribute_name)
        
        if isinstance(expected_value, list):
            # If expected_value is a list, check if actual_value is in the list
            assert actual_value in expected_value, \
                f"Attribute '{attribute_name}' mismatch: Expected one of {expected_value}, but got '{actual_value}'."
        else:
            # Otherwise, perform a direct equality check
            assert actual_value == expected_value, \
                f"Attribute '{attribute_name}' mismatch: Expected '{expected_value}', but got '{actual_value}'."

def test_password_field_displayed_correctly(page):
    login_page = LoginPage(page)
    login_page.navigate()

    assert login_page.password_input_field.is_visible(), "Password input field is not visible"

def test_password_field_attributes_correct(page):
    # Check type, name, autocomplete, required
    login_page = LoginPage(page)
    login_page.navigate()

    expected_attributes = {
        "type": "password",
        "name": "password",
        "autocomplete": "current-password",
        "required": "required"
    }

    for attribute_name, expected_value in expected_attributes.items():
        actual_value = login_page.get_password_input_attribute(attribute_name)
        
        assert actual_value == expected_value, \
            f"Attribute '{attribute_name}' mismatch: Expected '{expected_value}', but got '{actual_value}'"

def test_forgot_password_link_visible_and_enabled(page):
    login_page = LoginPage(page)
    login_page.navigate()

    expect(login_page.forgot_password_link).to_be_visible()
    expect(login_page.forgot_password_link).to_be_enabled()

def test_forgot_password_leads_to_forgot_password_page(page):
    login_page = LoginPage(page)
    login_page.navigate()

    login_page.click_forgot_password_link()

    expect(page).to_have_url("https://github.com/password_reset")

# --- Sign in tests ---
def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    # Not gonna do it right now with my credentials
    pass

def test_login_with_incorrect_password(page):
    login_page = LoginPage(page)
    login_page.navigate()

    login_page.login(VALID_USER, INVALID_PASSWORD)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("Incorrect username or password.")
    expect(page).to_have_url("https://github.com/login")

def test_login_with_nonexistent_username(page):
    login_page = LoginPage(page)
    login_page.navigate()

    login_page.login(INVALID_USER, INVALID_PASSWORD)

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_have_text("Incorrect username or password.")
    expect(page).to_have_url("https://github.com/login")

def test_login_with_empty_username(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(EMPTY_STRING, INVALID_PASSWORD)

    expect(page).to_have_url("https://github.com/login")

def test_login_with_empty_password(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(INVALID_USER, EMPTY_STRING)

    expect(page).to_have_url("https://github.com/login")

def test_login_with_special_characters_in_username(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_input_field.fill("user!@#$%^&*()_+")

    # Assert that the input field accepts these characters or shows validation
    expect(login_page.login_input_field).to_have_value("user!@#$%^&*()_+")

def test_username_field_gets_focus_on_load(page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    is_focused = login_page.login_input_field.evaluate("el => el === document.activeElement")

    assert is_focused, "The login input field did not receive focus on load."