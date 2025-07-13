class LoginPage:
    def __init__(self, page):
        self.page = page 

        # Locators of main elements
        self.main_header = page.locator("div.auth-form-header") # Sign in to Github
        self.login_input_field = page.locator("input#login_field")
        self.password_input_field = page.locator("input#password")
        self.forgot_password_link = page.locator("a#forgot-password")
        self.error_message = page.locator("div#js-flash-container")
        self.sign_in_button = page.locator("input[type='submit']")

    def navigate(self):
        self.page.goto(f"https://github.com/login")

    def get_main_header_text(self) -> str:
        return self.main_header.text_content().strip()
    
    def get_login_input_attribute(self, attribute_name: str) -> str:
        return self.login_input_field.get_attribute(attribute_name)
    
    def get_password_input_attribute(self, attribute_name: str) -> str:
        return self.password_input_field.get_attribute(attribute_name)
    
    def click_forgot_password_link(self):
        """
        Clicks the forgot password link with further navigation to forgot password page
        """
        self.forgot_password_link.click()
    
    def login(self, login, password):
        self.password_input_field.wait_for(state="visible")
        self.login_input_field.wait_for(state="visible")

        self.login_input_field.fill(login)
        self.password_input_field.fill(password)

        self.sign_in_button.wait_for(state="visible", timeout=10000)
        self.sign_in_button.click()
