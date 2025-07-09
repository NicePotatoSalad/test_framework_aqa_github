class LoginPage:
    def __init__(self, page):
        self.page = page 

        # Locators of main elements
        self.main_header = page.locator("div.auth-form-header") # Sign in to Github
        self.login_input_field = page.locator("input#login_field")

    def navigate(self):
        self.page.goto(f"https://github.com/login")

    def get_main_header_text(self) -> str:
        return self.main_header.text_content().strip()
    
    