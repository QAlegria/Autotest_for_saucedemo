import re

from playwright.sync_api import Page, expect, Locator
from playwright.sync_api import sync_playwright
from pages.locators.home_page_locators import HomePageLocators as Locators
from pages.parameters.home_page_parameters import HomePageParameters as Parameters


class BasePage:
    base_url = 'https://www.saucedemo.com/'
    page_url = None

    def __init__(self, page:Page):
        self.page = page

    def open(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened by this url')

    def find(self, locator) -> Locator:
        return self.page.locator(locator)

