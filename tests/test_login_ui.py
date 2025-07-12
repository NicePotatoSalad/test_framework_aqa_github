import pytest
import playwright 

from pages.login_page import LoginPage


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

def test_login_input_field_attributes_correct(page, type="text", name="login", \
                                        autocapitalize="off", autocorrect="off", \
                                        autocomplete="username", autofocus="autofocus", required="required"):
    # Check type, name, autocapitalize, autocorrect, autocomplete, autofocus, required
    login_page = LoginPage(page)
    login_page.navigate()

    expected_attributes = {
        "type": type,
        "name": name,
        "autocapitalize": autocapitalize,
        "autocorrect": autocorrect,
        "autocomplete": autocomplete,
        "autofocus": autofocus,
        "required": required
    }

    for attribute_name, expected_value in expected_attributes.items():
        actual_value = login_page.get_login_input_attribute()
        
        assert actual_value == expected_value, \
            f"Attribute '{attribute_name}' mismatch: Expected '{expected_value}', but got '{actual_value}'"

def test_password_field_displayed_correctly(page):
    login_page = LoginPage(page)
    login_page.navigate()

    assert login_page.password_input_field.is_visible(), "Password input field is not visible"

def test_password_field_attributes_correct(page, type="password", name="password", autocomplete="current-password", required="required"):
    # Check type, name, autocomplete, required
    login_page = LoginPage(page)
    login_page.navigate()

    expected_attributes = {
        "type": type,
        "name": name,
        "autocomplete": autocomplete,
        "required": required
    }

    for attribute_name, expected_value in expected_attributes.items():
        actual_value = login_page.get_password_input_attribute()
        
        assert actual_value == expected_value, \
            f"Attribute '{attribute_name}' mismatch: Expected '{expected_value}', but got '{actual_value}'"

def test_forgot_password_displayed(page):
    pass

def test_forgot_password_clickable(page):
    pass

def test_forgot_password_leads_to_forgot_password_page():
    pass



