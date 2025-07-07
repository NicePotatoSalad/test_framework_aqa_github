import pytest
from pages.profile_page import ProfilePage

# Замените 'YOUR_GITHUB_USERNAME' на ваш реальный никнейм на GitHub
# Для приватных данных используйте переменные окружения, но для MVP можно так
TEST_USERNAME = "NicePotatoSalad" 


# ---- Page Loaded Correctly ----

def test_additional_username_is_displayed(page, additional_username = "NicePotatoSalad"):
    profile_page = ProfilePage(page)
    profile_page.navigate(TEST_USERNAME)

    assert profile_page.get_additional_username() == additional_username, \
        f"Ожидалось имя пользователя '{additional_username}', получено '{profile_page.get_additional_username()}'"

def test_username_is_displayed(page, name="Greg"):
    profile_page = ProfilePage(page)
    profile_page.navigate(TEST_USERNAME)

    assert profile_page.get_username() == name, \
        f"Ожидалось имя пользователя '{name}', получено '{profile_page.get_username()}'"
    
def test_profile_bio_is_displayed(page, bio_text="Middle Full-Stack QA engineer | Game developer | Academic masochist"):
    profile_page = ProfilePage(page)
    profile_page.navigate(TEST_USERNAME)

    assert profile_page.get_bio_text() == bio_text,\
        f"Bio text is {profile_page.get_bio_text()}, but has to be {bio_text}"


# ---- Tabs ----

def test_overview_tab_is_visible(page):
    profile_page = ProfilePage(page)
    profile_page.navigate(TEST_USERNAME)

    assert profile_page.overview_tab.is_visible(), "Вкладка 'Overview' не видна"

def test_repositories_tab_is_visible(page):
    profile_page = ProfilePage(page)
    profile_page.navigate(TEST_USERNAME)

    assert profile_page.repositories_tab.is_visible(), "Вкладка 'repositories' не видна"

def test_projects_tab_is_visible(page):
    profile_page = ProfilePage(page)
    profile_page.navigate(TEST_USERNAME)

    assert profile_page.projects_tab.is_visible(), "Вкладка 'projects' не видна"

def test_packages_tab_is_visible(page):
    profile_page = ProfilePage(page)
    profile_page.navigate(TEST_USERNAME)

    assert profile_page.packages_tab.is_visible(), "Вкладка 'packages' не видна"

def test_stars_tab_is_visible(page):
    profile_page = ProfilePage(page)
    profile_page.navigate(TEST_USERNAME)

    assert profile_page.stars_tab.is_visible(), "Вкладка 'stars' не видна"

# ---- Navigation Tabs Work Correctly ----

def test_navigate_to_repositories_tab(page):
    profile_page = ProfilePage(page)
    profile_page.navigate(TEST_USERNAME)

    profile_page.click_the_repositories_tab()

    assert profile_page.repositories_tab.is_visible(), "Вкладка 'Repositories' исчезла после клика"

def test_navigate_to_projects_tab(page):
    profile_page = ProfilePage(page)
    profile_page.navigate(TEST_USERNAME)

    profile_page.click_the_projects_tab()

    assert profile_page.projects_tab.is_visible(), "Вкладка 'projects' исчезла после клика"

def test_navigate_to_packages_tab(page):
    profile_page = ProfilePage(page)
    profile_page.navigate(TEST_USERNAME)

    profile_page.click_the_packages_tab()

    assert profile_page.packages_tab.is_visible(), "Вкладка 'packages' исчезла после клика"

def test_navigate_to_stars_tab(page):
    profile_page = ProfilePage(page)
    profile_page.navigate(TEST_USERNAME)

    profile_page.click_the_stars_tab()

    assert profile_page.stars_tab.is_visible(), "Вкладка 'stars' исчезла после клика"