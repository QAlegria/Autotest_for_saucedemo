import re
from decimal import Decimal

from playwright.sync_api import expect

from config import setting
from pages.base_page import BasePage
from pages.components.cart_and_page_component import ExtendedPageComponents
from pages.components.footer_component import FooterComponents
from pages.components.left_menu_component import LeftMenu
from pages.components.navigation_component import BackAndContinue
from pages.components.product_component import CheckOutProducts
from pages.locators.checkout_second_page_locators import CheckOutSecondPageLocators as Locators
from utils.helpers import PriceHelper


class CheckOutSecondPage(BasePage):

    # Working with logo, cart_icon, title
    @property
    def page_components(self):
        return ExtendedPageComponents(self.page)

    # Working with left menu
    @property
    def left_menu(self):
        return LeftMenu(self.page)

    # Working wih product cards
    @property
    def products(self):
        return CheckOutProducts(self.page, self.network)


    # Working with product list
    @property
    def description_label(self):
        return self.find(Locators.description_label)

    def description_label_has_text(self, text):
        self.check_visibility_and_text(self.description_label, text)


    @property
    def cart_list(self):
        return self.find(Locators.list_of_cart_products)

    def check_cart_list_is_empty(self):
        expect(self.products.description.product_item).to_have_count(0)


    def check_prod_list_from_cart_page_is_right(self, prod_list):
        print(self.products.description.get_list_of_product_names())
        assert self.products.description.get_list_of_product_names() == prod_list


    # Working with information
    @property
    def payment_info_label_element(self):
        return self.find(Locators.payment_info_label)

    def payment_info_label_has_text(self, text):
        self.check_visibility_and_text(self.payment_info_label_element, text)

    @property
    def payment_info_value_element(self):
        return self.find(Locators.payment_info_value)

    def payment_info_value_has_text(self, text):
        self.check_visibility_and_text(self.payment_info_value_element, text)

    @property
    def shipping_info_label_element(self):
        return self.find(Locators.shipping_info_label)

    def shipping_info_label_has_text(self, text):
        self.check_visibility_and_text(self.shipping_info_label_element, text)

    @property
    def shipping_info_value_element(self):
        return self.find(Locators.shipping_info_value)

    def shipping_info_value_has_text(self, text):
        self.check_visibility_and_text(self.shipping_info_value_element, text)

    @property
    def total_price_label_element(self):
        return self.find(Locators.total_price_label)

    def total_price_label_has_text(self, text):
        self.check_visibility_and_text(self.total_price_label_element, text)

    @property
    def subtotal_price_label_element(self):
        return self.find(Locators.subtotal_price_label)

    def subtotal_price_label_has_text(self, text):
        self.check_visibility_and_text(self.subtotal_price_label_element, text, use_regex=True)

    @property
    def subtotal_price(self) -> Decimal:
        subtotal_price_str = self.subtotal_price_label_element.inner_text()
        return PriceHelper.get_decimal_price_from_text(subtotal_price_str, setting.SITE_CURRENCY)

    @property
    def tax_label_element(self):
        return self.find(Locators.tax_label)

    def tax_label_has_text(self, text):
        self.check_visibility_and_text(self.tax_label_element, text, use_regex=True)

    @property
    def tax_price(self) -> Decimal:
        return PriceHelper.tax_price(setting.TAX, self.products.description.get_sum_prices)

    @property
    def tax_price_from_page(self) -> Decimal:
        return PriceHelper.get_decimal_price_from_text(self.tax_label_element.inner_text(), setting.SITE_CURRENCY)

    @property
    def total_price_element(self):
        return self.find(Locators.total_price)

    def total_price_has_text(self, text):
        self.check_visibility_and_text(self.total_price_element, text, use_regex=True)

    @property
    def total_price_with_tax(self):
        total_price = self.tax_price + self.products.description.get_sum_prices
        return total_price

    @property
    def total_price_with_tax_from_page(self):
        return PriceHelper.get_decimal_price_from_text(self.total_price_element.inner_text(), setting.SITE_CURRENCY)


    # Working with price
    def check_subtotal_price_is_summing_right(self):
        sum_product_prices = self.products.description.get_sum_prices
        # print(subtotal_price, ' = ', sum_product_prices)
        assert self.subtotal_price == sum_product_prices, f'{self.subtotal_price} = {sum_product_prices}'

    def check_tax_is_counting_right(self):
        # print(self.tax_price, ' = ', self.tax_price_from_page)
        assert self.tax_price == self.tax_price_from_page

    def check_total_price_is_counting_right(self):
        print(self.total_price_with_tax, ' == ', self.total_price_with_tax_from_page)
        assert self.total_price_with_tax == self.total_price_with_tax_from_page




    # Working with navigation
    @property
    def navigation(self):
        return BackAndContinue(self.page)

    @property
    def cancel_btn(self):
        return self.navigation.back_btn

    def cancel_btn_has_text(self, text):
        self.check_visibility_and_text(self.cancel_btn, text)

    def click_cancel_btn(self):
        self.cancel_btn.click()

    @property
    def finish_btn(self):
        return self.navigation.continue_btn

    def finish_btn_has_text(self, text):
        self.check_visibility_and_text(self.finish_btn, text)

    def click_finish_btn(self):
        self.finish_btn.click()

    # Social media and terms elements
    @property
    def footer(self):
        return FooterComponents(self.page)