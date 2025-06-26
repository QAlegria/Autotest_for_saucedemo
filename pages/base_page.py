import re

from playwright.sync_api import Page, expect, Locator
from playwright.sync_api import sync_playwright

from config import setting
from pages.locators.home_page_locators import HomePageLocators as Locators
from pages.parameters.home_page_parameters import HomePageParameters as Parameters
from utils.network import NetworkWatcher
from typing import Optional


class BasePage:
    base_url = setting.HOME_PAGE_URL
    page_url = None

    def __init__(self, page:Page, network: Optional[NetworkWatcher] = None):
        self.page = page
        self.network = network

    def open(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened by this url')

    def find(self, locator) -> Locator:
        return self.page.locator(locator)

    def check_visibility_and_text(self, element, expected_text):
        expect(element).to_be_visible()
        expect(element).to_have_text(expected_text)

    def check_visibility_list_of_elements(self, list_of_elements):
        for element in range(list_of_elements.count()):
            expect(list_of_elements.nth(element)).to_be_visible()

    def check_visibility_and_attribute(self, element, attribute_name, attribute_value):
        expect(element).to_be_visible()
        expect(element).to_have_attribute(attribute_name, attribute_value)