# pages/profile_page.py

class ProfilePage:
    """
    Page Object Model для страницы профиля пользователя GitHub.
    Инкапсулирует локаторы элементов и методы взаимодействия с ними.
    """

    def __init__(self, page):
        self.page = page
        # Локаторы основных элементов страницы профиля
        self.additional_username = page.locator("h1.vcard-names span.p-nickname") # NicePotatoSalad
        self.username = page.locator("h1.vcard-names span.p-name") # Greg
        self.bio_text = page.locator("div.p-note.user-profile-bio")


        # Tabs
        self.overview_tab = page.get_by_role("link", name="Overview") # Overview tab
        self.repositories_tab = page.get_by_role("link", name="Repositories") # Repositories tab
        self.projects_tab = page.get_by_role("link", name="Projects") # Projects tab
        self.packages_tab = page.get_by_role("link", name="Packages") # Packages tab
        self.stars_tab = page.get_by_role("link", name="stars") # Stars tab


    def navigate(self, username: str):
        """Переходит на страницу профиля по имени пользователя."""
        self.page.goto(f"https://github.com/{username}")

    def get_additional_username(self) -> str:
        """Возвращает никнейм пользователя из заголовка профиля."""
        return self.additional_username.text_content().strip()

    def get_username(self) -> str:
        """Возвращает имя пользователя из заголовка профиля."""
        return self.username.text_content().strip()
    
    def get_bio_text(self) -> str:
        """"Returnes the user bio text"""
        if self.bio_text.is_visible():
            return self.bio_text.text_content().strip()
        return ""
    
    def click_the_repositories_tab(self):
        self.repositories_tab.click()
        self.page.wait_for_load_state('networkidle')

    def click_the_projects_tab(self):
        self.projects_tab.click()
        self.page.wait_for_load_state('networkidle')

    def click_the_packages_tab(self):
        self.packages_tab.click()
        self.page.wait_for_load_state('networkidle')
    
    def click_the_stars_tab(self):
        self.stars_tab.click()
        self.page.wait_for_load_state('networkidle')

    
