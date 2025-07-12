class LoginPage:
    def __init__(self, page):
        self.page = page 

        # Locators of main elements
        self.main_header = page.locator("div.auth-form-header") # Sign in to Github
        self.login_input_field = page.locator("input#login_field")
        self.password_input_field = page.locator("input#password")

    def navigate(self):
        self.page.goto(f"https://github.com/login")

    def get_main_header_text(self) -> str:
        return self.main_header.text_content().strip()
    
    def get_login_input_attribute(self, attribute_name: str) -> str:
        return self.login_input_field.get_attribute(attribute_name)
    
    def get_password_input_attribute(self, attribute_name: str) -> str:
        return self.password_input_field.get_attribute(attribute_name)