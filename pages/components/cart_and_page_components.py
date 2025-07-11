import allure

from config.static_image_name import ImageName
from pages.base_page import BasePage
from pages.locators.components.cart_and_page_components import PageComponentsLocators as Locators
from playwright.sync_api import expect


class PageComponents(BasePage):

    @property
    def page_logo(self):
        return self.find(Locators.page_logo)

    def page_logo_is_displayed_and_has_text(self, text):
        self.check_visibility_and_text(self.page_logo, text)


    # Working with shopping cart
    @property
    def shopping_cart_icon(self):
        return self.find(Locators.shopping_cart)

    @allure.step("Click on shopping cart button")
    def click_shopping_cart(self):
        self.shopping_cart_icon.click()

    def shopping_cart_icon_is_displayed(self):
        expect(self.shopping_cart_icon).to_be_visible()

    def shopping_cart_image_is_on_page(self):
        self.check_element_image_link(self.shopping_cart_icon, ImageName.shopping_card_image_name)

    @property
    def shopping_cart_counter(self):
        return self.find(Locators.shopping_cart_counter)

    def check_product_counter_icon_is_not_displayed(self):
        expect(self.shopping_cart_counter).not_to_be_attached()


    @allure.step("Checking count shopping cart icon")
    def check_product_counter_icon_is(self, count):
        if count == 0:
            self.check_product_counter_icon_is_not_displayed()
        else:
            self.check_visibility_and_text(self.shopping_cart_counter, str(count))


class ExtendedPageComponents(PageComponents):
    # Product title label
    @property
    def page_title(self):
        return self.find(Locators.title)

    def header_of_product_title_has_text(self, text):
        self.check_visibility_and_text(self.page_title, text)
