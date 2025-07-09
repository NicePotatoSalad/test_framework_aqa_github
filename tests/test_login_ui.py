import pytest
import playwright 

from pages.login_page import LoginPage


def test_main_header_displayed_correctly(page, text="Sign in to GitHub"):
    login_page = LoginPage(page)
    login_page.navigate()

    assert login_page.main_header.is_visible(), "Main header is not visible"
    assert login_page.get_main_header_text() == text, \
        f"Main header text is expected to be {text}, but got {login_page.get_main_header_text}"
    
def test_input_field_displayed_correctly(page):
    login_page = LoginPage(page)
    login_page.navigate()

    assert login_page.login_input_field.is_visible(), "Login input field is not visible"

def test_input_field_attributes_correct(page):
    # Check type, name, autocapitalize, autocorrect, autocomplete, autofocus, required

    
    pass

def test_password_field_displayed_correctly(page):
    pass

def test_password_field_attributes_correct(page):
    # Check type, name, autocomplete, required
    pass

def test_forgot_password_displayed(page):
    pass

def test_forgot_password_clickable(page):
    pass

def test_forgot_password_leads_to_forgot_password_page():
    pass



