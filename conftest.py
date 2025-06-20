import pytest
from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.inventory_page import InventoryPage
from faker import Faker
from pages.base_page import BasePage
from pages.locators.home_page_locators import HomePageLocators
from utils.expect_visible_helpers import ExpectVisibleElements
from pages.parameters.credentials import Password, StandardUser
from api.image_api import ImageApi
from config import setting


@pytest.fixture()
def checking_main_page(page):
    return HomePage(page)

# Is this correct?
@pytest.fixture()
def auth_session_with_standard_user(page:Page):
    page.goto(BasePage.base_url)
    page.fill(HomePageLocators.username_field, StandardUser.standard_username)
    page.fill(HomePageLocators.password_field, Password.password)
    page.click(HomePageLocators.login_button)
    page.wait_for_url(f'**{setting.INVENTORY_PAGE_URL}')
    return page

@pytest.fixture()
def checking_inventory_page(auth_session_with_standard_user):
    return InventoryPage(auth_session_with_standard_user)


@pytest.fixture()
def wrong_username():
    fake = Faker()
    return fake.user_name()

@pytest.fixture()
def standard_user():
    standard_user = StandardUser.standard_username
    return standard_user

@pytest.fixture()
def valid_password():
    valid_password = Password.password
    return valid_password

@pytest.fixture()
def invalid_password():
    fake = Faker()
    return fake.password()

@pytest.fixture()
def get_image_api():
    ImageApi()
