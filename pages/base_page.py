import re

from playwright.sync_api import Page, expect, Locator
from playwright.sync_api import sync_playwright

from config import setting
from pages.locators.home_page_locators import HomePageLocators as Locators
from pages.parameters.home_page_parameters import HomePageParameters as Parameters
from utils.network import NetworkWatcher
from typing import Optional, Literal


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

    def find(self, selector) -> Locator:
        return self.page.locator(selector)

    def find_by_index(self, locator, index) -> Locator:
        return self.find(locator).nth(index)

    def open_new_tab_with_click(self, locator, wait_state: Literal["load", "domcontentloaded", "networkidle"] = "load"):
        with self.page.context.expect_page() as new_tab_info:
            locator.click()
        new_page = new_tab_info.value
        new_page.wait_for_load_state(wait_state)
        return new_page

    # def list_of_elements(self, elements: Locator):
    #     count = elements.count()
    #     return [elements.nth(count).inner_text() for i in range(count)]

    def check_visibility_and_text(self, element, expected_text):
        expect(element).to_be_visible()
        expect(element).to_have_text(expected_text)

    def check_visibility_list_of_elements(self, list_of_elements):
        for element in range(list_of_elements.count()):
            expect(list_of_elements.nth(element)).to_be_visible()

    def check_visibility_and_attribute(self, element, attribute_name, attribute_value):
        expect(element).to_be_visible()
        expect(element).to_have_attribute(attribute_name, attribute_value)

    def check_element_image_link(self, element, image_name):
        image_link_from_element = element.evaluate("element => getComputedStyle(element).backgroundImage")
        expected_image_link = f'{setting.STATIC_IMAGE_URL}{image_name}'
        assert expected_image_link in image_link_from_element,f"Mismatch between expected_image_link {expected_image_link} and image_link_from_element {image_link_from_element} from page"

    def check_static_image_request(self, method, image_name):
        self.network.check_image_response_body_by_method_url(method, image_name)