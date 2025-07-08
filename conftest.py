import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.inventory_page import InventoryPage
from faker import Faker
from pages.base_page import BasePage
from pages.locators.home_page_locators import HomePageLocators
from pages.page_swither import PageSwitcher
from pages.parameters.credentials import Password, StandardUser, LockedOutUser, PerformanceGlitchUser, ProblemUser, ErrorUser, VisualUser
from api.image_api import ImageApi
from config import setting
from utils.network import NetworkWatcher


@pytest.fixture()
def main_page(page):
    return HomePage(page)


@pytest.fixture()
def inventory_page(page:Page):
    page.goto(BasePage.base_url)
    page.fill(HomePageLocators.username_field, StandardUser.standard_username)
    page.fill(HomePageLocators.password_field, Password.password)
    network = NetworkWatcher(page)
    network.start_tracking()
    page.click(HomePageLocators.login_button)
    page.wait_for_url(f'**{setting.INVENTORY_PAGE_URL}')
    page.wait_for_load_state("load")
    return InventoryPage(page, network)

@pytest.fixture()
def cart_page(inventory_page, page_switcher):
    page_switcher.switch_to_cart_page()
    return CartPage(inventory_page.page)


@pytest.fixture()
def page_switcher(page):
    return PageSwitcher(page)



@pytest.fixture()
def wrong_username():
    fake = Faker()
    return fake.user_name()

@pytest.fixture()
def standard_user():
    return StandardUser.standard_username

@pytest.fixture()
def locked_out_user():
    return LockedOutUser.locked_out_username

@pytest.fixture()
def problem_user():
    return ProblemUser.problem_username

@pytest.fixture()
def performance_glitch_user():
    return PerformanceGlitchUser.performance_glitch_username

@pytest.fixture()
def visual_user():
    return VisualUser.visual_username

@pytest.fixture()
def error_user():
    return ErrorUser.error_username

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
    return ImageApi()

@pytest.fixture()
def prod_list():
    return []

