from decimal import Decimal

import allure

from pages.base_page import BasePage
from playwright.sync_api import expect

from pages.locators.cart_page_locators import CartPageLocators
from pages.locators.components.product_component_locators import ProductComponentLocators as Locators
from pages.locators.inventory_page_locators import InventoryPageLocators
from pages.parameters.components.product_parameters import ProductParameters
from pages.parameters.inventory_page_parameters import InventoryPageParameters
from utils.helpers import PriceHelper
from utils.json_worker import JsonWorker


class Description(BasePage):

    # Working with product cards
    @property
    def all_product_names(self):
        return self.find(Locators.product_name_header)

    def get_list_of_product_names(self):
        return self.all_product_names.all_inner_texts()

    @property
    def product_item(self):
        return self.find(Locators.product_item)

    def get_product_item_count(self):
        return self.product_item.count()

    def product_item_by_index(self, index):
        return self.find_by_index(Locators.product_item, index)

    # Prices
    @property
    def all_product_prices(self):
        return self.find(Locators.product_price)

    def get_list_of_product_prices(self) -> Decimal:
        return PriceHelper.get_decimal_prices(self.all_product_prices.all_inner_texts())

    @property
    def get_sum_prices(self):
        return PriceHelper.sum_product_prices(self.get_list_of_product_prices())

    # Searching by index
    def product_name_header_by_index(self, index):
        return self.find_by_index(Locators.product_name_header, index)

    def nth_product_name_is_displayed(self, index):
        expect(self.product_name_header_by_index(index)).to_be_visible()

    def get_product_name_by_index(self, index):
        return self.product_name_header_by_index(index).inner_text()

    def click_on_selected_product(self, index):
        product_name = self.get_product_name_by_index(index)
        self.product_name_header_by_index(index).click()
        return product_name


    def product_description_by_index(self, index):
        return self.find_by_index(Locators.product_description, index)

    def nth_product_description_is_displayed(self, index):
        expect(self.product_description_by_index(index)).to_be_visible()

    def get_product_description_by_index(self, index):
        return self.product_description_by_index(index).inner_text()


    def product_price_by_index(self, index):
        return self.find_by_index(Locators.product_price, index)

    def nth_product_price_is_displayed(self, index):
        expect(self.product_price_by_index(index)).to_be_visible()

    def get_product_price_and_currency_text_by_index(self, index):
        return self.product_price_by_index(index).inner_text()

    def get_product_price_by_index(self, index):
        return PriceHelper.get_product_price(self.get_product_price_and_currency_text_by_index(index))

    def get_product_currency_by_index(self, index):
        return PriceHelper.get_product_price_currency(self.get_product_price_and_currency_text_by_index(index))

    def get_product_data_by_index(self, index):
        data = {
            "name": self.get_product_name_by_index(index),
            "description": self.get_product_description_by_index(index),
            "price": self.get_product_price_by_index(index),
            "currency": self.get_product_currency_by_index(index)
        }
        if hasattr(self, "get_product_image_url_by_index"):
            data["image_url"] =  self.get_product_image_url_by_index(index)
        return data

    @allure.step("Checking that product on page is in expected product json")
    def check_product_by_index_is_in_json(self, index, json):
        product_json_filter = JsonWorker()
        product_json_filter.open_file(json)
        data = self.get_product_data_by_index(index)
        product_items_for_name = product_json_filter.get_product_by_conditions(**data)
        assert product_items_for_name, \
            (f"Mismatch between product on page\n"
             f"{data.get('name')}\n"
             f"{data.get('description')}\n"
             f"{data.get('image_url', 'no image')}\n"
             f"{data.get('price')}\n"
             f"{data.get('currency')}\n and product in JSON")


    def check_all_product_is_in_json(self, json):
        product_json_filter = JsonWorker()
        product_json_filter.open_file(json)
        for index in range(self.get_product_item_count()):
            data = self.get_product_data_by_index(index)
            product_items_for_name = product_json_filter.get_product_by_conditions(**data)
            assert product_items_for_name, \
                (f"Mismatch between product on page\n"
                 f"{data.get('name')}\n"
                 f"{data.get('description')}\n"
                 f"{data.get('image_url', 'no image')}\n"
                 f"{data.get('price')}\n"
                 f"{data.get('currency')}\n and product in JSON")

class ExtendedDescription(Description):

    @property
    def qty_label(self):
        return self.find(Locators.qty_label)

    def qty_label_has_text(self, text):
        self.check_visibility_and_text(self.qty_label, text)

    @property
    def description_label(self):
        return self.find(Locators.description_label)

    def description_label_has_text(self, text):
        self.check_visibility_and_text(self.description_label, text)

    def product_qty_by_index(self, index):
        return self.find_by_index(Locators.cart_quantity, index)

    def nth_product_qty_has_text(self,index, text):
        self.check_visibility_and_text(self.product_qty_by_index(index), text)

class RemoveButton(BasePage):
    # Button remove from cart
    @property
    def get_product_remove_from_cart_btn_count(self) -> int:
        return self.find(Locators.button_to_remove_from_cart).count()

    def remove_from_cart_element(self, index):
        return self.find_by_index(Locators.button_to_remove_from_cart, index)

    def button_remove_from_cart_by_index_is_displayed(self, index):
        self.check_visibility_and_text(self.remove_from_cart_element(index), ProductParameters.remove_from_cart)

    def button_remove_from_cart_by_index_is_not_displayed(self, index):
        expect(self.remove_from_cart_element(index)).not_to_be_attached()

    @allure.step("Clicking on remove product button and return removed product name")
    def click_button_remove_from_cart_product_by_index(self, index):
        name_of_product = self.remove_from_cart_element(index).locator(Locators.nearest_item).locator(Locators.product_name_header).inner_text()
        self.remove_from_cart_element(index).click()
        print(name_of_product)
        return name_of_product


class ImageComponent(Description):

    def product_image_by_index(self, index):
        return self.find_by_index(Locators.product_image, index)

    def nth_product_image_is_displayed(self, index):
        expect(self.product_image_by_index(index)).to_be_visible()

    def check_image_name_matches_product_name_by_index(self, index):
        assert self.get_product_image_url_by_index(index) == self.get_product_name_by_index(index), "Mismatch between product name and product name in image"

    def get_name_of_product_image_by_index(self, index):
        return self.product_image_by_index(index).get_attribute('alt')

    def get_product_image_url_by_index(self, index):
        return self.product_image_by_index(index).get_attribute('src')

    @allure.step("Checking that request of product image was called")
    def check_was_request_of_product_image_called_by_index(self, index):
        url = self.get_product_image_url_by_index(index)
        assert self.network.was_url_requested(url=url), f'The specified request was not requested {url}'


class AddButton(BasePage):
    # Button add to cart
    @property
    def get_product_add_btn_count(self) -> int:
        return self.find(InventoryPageLocators.button_add_to_cart).count()

    def add_to_cart_element(self, index):
        return self.find_by_index(InventoryPageLocators.button_add_to_cart, index)

    def button_add_to_cart_by_index_is_displayed(self, index):
        self.check_visibility_and_text(self.add_to_cart_element(index), InventoryPageParameters.add_to_cart)

    @allure.step("Clicking on product add to cart button and return name of added product")
    def click_button_add_to_card_product_by_index(self, index):
        name_of_product = self.add_to_cart_element(index).locator(Locators.nearest_item).locator(Locators.product_name_header).inner_text()
        self.add_to_cart_element(index).click()
        return name_of_product


class InventoryProducts(BasePage):
    def __init__(self, page, network):
        self.page = page
        self.network = network

        self.description = ImageComponent(self.page, self.network)
        self.add_button = AddButton(self.page)
        self.remove_button = RemoveButton(self.page)


class CartProducts(BasePage):
    def __init__(self, page, network):
        self.page = page
        self.network = network

        self.description = ExtendedDescription(self.page)
        self.remove_button = RemoveButton(self.page)


class CheckOutProducts(BasePage):
    def __init__(self, page, network):
        self.page = page
        self.network = network

        self.description = ExtendedDescription(self.page)


class InventoryItem(InventoryProducts):

    def get_product_name(self):
        return self.description.get_product_name_by_index(0)

    def get_product_description(self):
        return self.description.get_product_description_by_index(0)

    def get_product_price(self):
        return self.description.get_product_price_by_index(0)

    def get_product_currency(self):
        return self.description.get_product_currency_by_index(0)

    def get_product_image_url(self):
        return self.description.get_product_image_url_by_index(0)

    def __click_add_to_cart(self):
        return self.add_button.click_button_add_to_card_product_by_index(0)

    def click_add_to_cart(self, prod_list: list):
        prod_list.append(self.__click_add_to_cart())

    def button_add_to_cart_is_displayed(self):
        return self.add_button.button_add_to_cart_by_index_is_displayed(0)

    def button_remove_to_cart_is_displayed(self):
        return self.remove_button.button_remove_from_cart_by_index_is_displayed(0)

    def button_remove_to_cart_is_not_displayed(self):
        return self.remove_button.button_remove_from_cart_by_index_is_not_displayed(0)

    def __click_remove_from_cart(self):
        return self.remove_button.click_button_remove_from_cart_product_by_index(0)

    def click_remove_from_cart(self, prod_list: list):
        prod_list.remove(self.__click_remove_from_cart())

    def check_product_is_in_json(self, json):
        data = {
            "name": self.get_product_name(),
            "description": self.get_product_description(),
            "price": self.get_product_price(),
            "currency": self.get_product_currency(),
        }
        if hasattr(self, "get_product_image_url"):
            data["image_url"] = self.get_product_image_url()

        product_json_filter = JsonWorker()
        product_json_filter.open_file(json)
        product_items = product_json_filter.get_product_by_conditions(**data)
        assert product_items, (
            f"Mismatch between product on page:\n"
            f"{data.get('name')}\n"
            f"{data.get('description')}\n"
            f"{data.get('image_url', 'no image')}\n"
            f"{data.get('price')}\n"
            f"{data.get('currency')}\n and product in JSON"
        )