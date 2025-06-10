import pytest
from playwright.sync_api import BrowserContext
from pages.home_page import HomePage
from faker import Faker

@pytest.fixture()
def checking_main_page(page):
    return HomePage(page)


@pytest.fixture()
def wrong_username():
    fake = Faker()
    return fake.user_name()

@pytest.fixture()
def standard_user():
    standard_user = 'standard_user'
    return standard_user

@pytest.fixture()
def valid_password():
    valid_password = 'secret_sauce'
    return valid_password

@pytest.fixture()
def invalid_password():
    fake = Faker()
    return fake.password()

