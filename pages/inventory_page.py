from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.parameters.inventory_page_parameters import InventoryPageParameters as Parameters
from pages.locators.inventory_page_locators import InventoryPageLocators as Locators
from utils.json_worker import JsonWorker
from config import setting
from utils.helpers import PriceHelper


class InventoryPage(BasePage):

    @property
    def inventory_page_logo(self):
        return self.find(Locators.inventory_page_logo)

    def inventory_page_logo_is_displayed_and_has_text(self, text):
        self.check_visibility_and_text(self.inventory_page_logo, text)

    @property
    def shopping_cart_image(self):
        return self.find(Locators.shopping_cart)

    def shopping_cart_image_is_displayed(self):
        expect(self.shopping_cart_image).to_be_visible()

    def shopping_cart_image_is_on_page(self):
        self.check_element_image_link(self.shopping_cart_image,Parameters.shopping_card_image_name)


    @property
    def left_menu_button(self):
        return self.find(Locators.left_menu_button)

    def left_menu_button_is_displayed(self):
        expect(self.left_menu_button).to_be_visible()

    def click_left_menu_button(self):
        self.left_menu_button.click()

    @property
    def button_to_close_left_menu(self):
        return self.find(Locators.button_to_close_left_menu)

    def click_close_button(self):
        self.button_to_close_left_menu.click()

    @property
    def button_to_main_menu(self):
        return self.find(Locators.button_to_main_menu)

    @property
    def button_about(self):
        return self.find(Locators.button_about)

    @property
    def logout_button(self):
        return self.find(Locators.logout_button)

    @property
    def reset_button(self):
        return self.find(Locators.reset_button)

    def button_to_main_menu_is_displayed(self):
        expect(self.button_to_main_menu).to_be_visible()

    def click_button_to_main_menu(self):
        self.button_to_main_menu.click()

    def button_about_is_displayed(self):
        expect(self.button_about).to_be_visible()

    def click_button_about(self):
        self.button_about.click()

    def logout_button_is_displayed(self):
        expect(self.logout_button).to_be_visible()

    def click_logout_button(self):
        self.logout_button.click()

    def reset_button_is_displayed(self):
        expect(self.reset_button).to_be_visible()

    def click_reset_button(self):
        self.reset_button.click()

    @property
    def product_filter(self):
        return self.find(Locators.product_filter)

    def filter_is_displayed(self):
        expect(self.product_filter).to_be_visible()

    def click_filter(self):
        self.product_filter.click()

    @property
    def header_of_product_title(self):
        return self.find(Locators.header_of_product_title)

    def header_of_product_title_has_text(self, text):
        self.check_visibility_and_text(self.header_of_product_title, text)

    def product_name_header_by_index(self, index):
        return self.find_by_index(Locators.product_name_header, index)

    def nth_product_name_is_displayed(self, index):
        expect(self.product_name_header_by_index(index)).to_be_visible()

    def product_description_by_index(self, index):
        return self.find_by_index(Locators.product_description, index)

    def nth_product_description_is_displayed(self, index):
        expect(self.product_description_by_index(index)).to_be_visible()

    def product_image_by_index(self, index):
        return self.find_by_index(Locators.product_image, index)

    def nth_product_image_is_displayed(self, index):
        expect(self.product_image_by_index(index)).to_be_visible()

    def product_price_by_index(self, index):
        return self.find_by_index(Locators.product_price, index)

    def nth_product_price_is_displayed(self, index):
        expect(self.product_price_by_index(index)).to_be_visible()

    def get_name_of_product_image_by_index(self, index):
        return self.product_image_by_index(index).get_attribute('alt')

    def get_product_image_url_by_index(self, index):
        return self.product_image_by_index(index).get_attribute('src')

    def get_product_name_by_index(self, index):
        return self.product_name_header_by_index(index).inner_text()

    def get_product_description_by_index(self, index):
        return self.product_description_by_index(index).inner_text()

    def check_image_name_matches_product_name_by_index(self, index):
        assert self.get_product_image_url_by_index(index) == self.get_product_name_by_index(index), "Mismatch between product name and product name in image"

    def get_product_price_and_currency_text_by_index(self, index):
        return self.product_price_by_index(index).inner_text()

    def get_product_price_by_index(self, index):
        return PriceHelper.get_price(self.get_product_price_and_currency_text_by_index(index))

    def get_product_currency_by_index(self, index):
        return PriceHelper.get_currency(self.get_product_price_and_currency_text_by_index(index))

    def check_product_by_index_is_in_json(self, index, json):
        product_json_filter = JsonWorker()
        product_json_filter.open_file(json)
        product_items_for_name = product_json_filter.get_product_by_conditions(
            name=self.get_product_name_by_index(index),
            description=self.get_product_description_by_index(index),
            image_url = self.get_product_image_url_by_index(index),
            price = self.get_product_price_by_index(index),
            currency = self.get_product_currency_by_index(index))
        assert product_items_for_name,"Mismatch between product on page and product in JSON"

    def checking_requests_of_products_image(self, url):
        self.network.was_url_requested(url)
