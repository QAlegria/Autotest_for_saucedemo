import allure
from playwright.sync_api import expect, BrowserContext
from pages.base_page import BasePage
from pages.components.footer_components import FooterComponents
from pages.components.left_menu_component import LeftMenu
from pages.parameters.cart_page_parameters import CartPageParameters as Parameters
from pages.locators.cart_page_locators import CartPageLocators as Locators
from utils.json_worker import JsonWorker
from utils.helpers import PriceHelper, ProductSort, RandomItems

class CartPage(BasePage):

    @property
    def cart_page_logo(self):
        return self.find(Locators.cart_page_logo)

    def inventory_page_logo_is_displayed_and_has_text(self, text):
        self.check_visibility_and_text(self.cart_page_logo, text)

    # Working with left menu
    @property
    def left_menu(self):
        return LeftMenu(self.page)


    # YourCart label
    @property
    def your_cart_label(self):
        return self.find(Locators.your_cart_title)

    def your_cart_label_has_text(self, text):
        self.check_visibility_and_text(self.your_cart_label, text)


    # Working with products
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

    @property
    def cart_list(self):
        return self.find(Locators.list_of_cart_products)

    @property
    def cart_item(self):
        return self.find(Locators.cart_product_container)

    def get_cart_item_count(self):
        return self.cart_item.count()

    def cart_item_by_index(self, index):
        return self.find_by_index(Locators.cart_product_container, index)

    def check_cart_list_is_empty(self):
        expect(self.cart_item).to_have_count(0)



    @property
    def all_product_names(self):
        return self.find(Locators.product_name_header)

    def get_list_of_product_names(self):
        return self.all_product_names.all_inner_texts()

    @property
    def all_product_prices(self):
        return self.find(Locators.product_price)

    def get_list_of_product_prices(self):
        return PriceHelper.get_float_prices(self.all_product_prices.all_inner_texts())


    # Searching product elements by index:

    def product_name_header_by_index(self, index):
        return self.find_by_index(Locators.product_name_header, index)

    def nth_product_name_is_displayed(self, index):
        expect(self.product_name_header_by_index(index)).to_be_visible()

    def product_description_by_index(self, index):
        return self.find_by_index(Locators.product_description, index)

    def nth_product_description_is_displayed(self, index):
        expect(self.product_description_by_index(index)).to_be_visible()

    def product_qty_by_index(self, index):
        return self.find_by_index(Locators.cart_quantity, index)

    def nth_product_qty_has_text(self,index, text):
        self.check_visibility_and_text(self.product_qty_by_index(index), text)

    def product_price_by_index(self, index):
        return self.find_by_index(Locators.product_price, index)

    def nth_product_price_is_displayed(self, index):
        expect(self.product_price_by_index(index)).to_be_visible()

    def get_product_name_by_index(self, index):
        return self.product_name_header_by_index(index).inner_text()

    def get_product_description_by_index(self, index):
        return self.product_description_by_index(index).inner_text()

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
            price = self.get_product_price_by_index(index),
            currency = self.get_product_currency_by_index(index))
        assert product_items_for_name,(f"Mismatch between product on page\n {self.get_product_name_by_index(index)}\n"
                                       f"{self.get_product_description_by_index(index)}\n ,"
                                       f"{self.get_product_price_by_index(index)}\n ,"
                                       f"{self.get_product_currency_by_index(index)}\n and product in JSON")

    def check_all_product_is_in_json(self, json):
        product_json_filter = JsonWorker()
        product_json_filter.open_file(json)
        for index in range(self.get_cart_item_count()):
            product_items_for_name = product_json_filter.get_product_by_conditions(
                name=self.get_product_name_by_index(index),
                description=self.get_product_description_by_index(index),
                price=self.get_product_price_by_index(index),
                currency=self.get_product_currency_by_index(index))
            assert product_items_for_name,(f"Mismatch between product on page\n {self.get_product_name_by_index(index)}\n"
                                       f"{self.get_product_description_by_index(index)}\n ,"
                                       f"{self.get_product_price_by_index(index)}\n ,"
                                       f"{self.get_product_currency_by_index(index)}\n and product in JSON")

    def check_prod_list_from_inventory_page_is_right(self, prod_list):
        print(self.get_list_of_product_names())
        assert self.get_list_of_product_names() == prod_list

    # Button remove from cart
    @property
    def get_product_remove_from_cart_btn_count(self) -> int:
        return self.find(Locators.button_to_remove_from_cart).count()

    def remove_from_cart_element(self, index):
        return self.find_by_index(Locators.button_to_remove_from_cart, index)

    def button_remove_from_cart_by_index_is_displayed(self, index):
        self.check_visibility_and_text(self.remove_from_cart_element(index), Parameters.remove_from_cart)

    def click_button_remove_from_cart_product_by_index(self, index):
        name_of_product = self.remove_from_cart_element(index).locator(Locators.nearest_product_card).locator(Locators.product_name_header).inner_text()
        self.remove_from_cart_element(index).click()
        print(name_of_product)
        return name_of_product


    # Working with navigation
    @property
    def continue_shopping_btn(self):
        return self.find(Locators.btn_continue_shop)

    def click_continue_shopping_btn(self):
        self.continue_shopping_btn.click()

    @property
    def checkout_btn(self):
        return self.find(Locators.btn_checkout)

    def click_checkout_btn(self):
        self.checkout_btn.click()


    # Social media and terms elements
    @property
    def footer(self):
        return FooterComponents(self.page)
