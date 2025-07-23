import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_first_page import CheckOutFirstPage
from pages.checkout_second_page import CheckOutProducts, CheckOutSecondPage
from pages.home_page import HomePage
from pages.inventory_page import InventoryPage
from pages.inventory_item_page import InventoryItemPage
from faker import Faker
from pages.base_page import BasePage
from pages.locators.home_page_locators import HomePageLocators
from pages.page_switcher import PageSwitcher
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
def check_out_first_page(cart_page, page_switcher):
    page_switcher.switch_to_check_out_first_page()
    return CheckOutFirstPage(cart_page.page)

@pytest.fixture()
def check_out_second_page(check_out_first_page, page_switcher):
    page_switcher.switch_to_check_out_second_page()
    return CheckOutSecondPage(check_out_first_page.page)



@pytest.fixture()
def random_inventory_item_locator_and_name(inventory_page):
    product_locator, product_name = inventory_page.get_random_product_name_locator()
    return product_locator, product_name

@pytest.fixture()
def random_inventory_item_page(inventory_page, page_switcher, random_inventory_item_locator_and_name):
    product_locator, product_name = random_inventory_item_locator_and_name
    page_switcher.switch_to_inventory_item_page(product_locator)
    return InventoryItemPage(inventory_page.page)

@pytest.fixture()
def selected_random_product_name(random_inventory_item_locator_and_name):
    product_locator, product_name = random_inventory_item_locator_and_name
    return product_name

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
def first_name():
    fake = Faker()
    return fake.first_name()

@pytest.fixture()
def last_name():
    fake = Faker()
    return fake.last_name()

@pytest.fixture()
def postal_code():
    fake = Faker()
    return fake.postalcode()

@pytest.fixture()
def get_image_api():
    return ImageApi()

@pytest.fixture()
def prod_list():
    return []

