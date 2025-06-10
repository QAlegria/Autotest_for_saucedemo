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