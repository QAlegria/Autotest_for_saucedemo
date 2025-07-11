from functools import cached_property, partial

import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.components.cart_and_page_components import ExtendedPageComponents
from pages.components.footer_components import FooterComponents
from pages.components.left_menu_component import LeftMenu
from pages.components.product_components import ProductComponents, InventoryProducts
from pages.parameters.inventory_page_parameters import InventoryPageParameters as Parameters
from pages.locators.inventory_page_locators import InventoryPageLocators as Locators
from utils.json_worker import JsonWorker
from config import setting
from utils.helpers import PriceHelper, ProductSort, RandomItems


class InventoryPage(BasePage):

    # Working with logo, cart_icon, title
    @property
    def page_components(self):
        return ExtendedPageComponents(self.page)

    # Checking cart icon counter
    def check_product_counter_icon_is_equals_random_selected_products(self):
        self.check_visibility_and_text(self.page_components.shopping_cart_counter, str(self.get_random_times_for_add_iteration))

    def check_product_counter_icon_is_equals_selected_minus_removed_products(self):
        if self.get_random_times_for_add_iteration - self.get_random_times_for_remove_iteration == 0:
            self.page_components.check_product_counter_icon_is_not_displayed()
        else:
            self.check_visibility_and_text(self.page_components.shopping_cart_counter, str(self.get_random_times_for_add_iteration-self.get_random_times_for_remove_iteration))

    # Working with left menu
    @property
    def left_menu(self):
        return LeftMenu(self.page)


    # Working with product cards
    @property
    def products(self):
        return InventoryProducts(self.page, self.network)



    # Working with sort AZ
    @allure.step("Checking that product on page is A to Z sorted")
    def check_products_is_a_to_z_sorted(self):
        assert ProductSort.a_to_z_sort(self.products.get_list_of_product_names()),\
            f"{self.products.get_list_of_product_names()}\n Products on page isn't A to Z sorted"

    @allure.step("Checking that product on page is Z to A sorted")
    def check_products_is_z_to_a_sorted(self):
        assert ProductSort.z_to_a_sort(self.products.get_list_of_product_names()),\
            f"{self.products.get_list_of_product_names()}\n Products on page isn't Z to A sorted"


    # Working with sort LH
    @allure.step("Checking that product on page is low to high sorted")
    def check_low_to_high_products_sort(self):
        assert ProductSort.low_to_high_sort(self.products.get_list_of_product_prices()), f"{self.products.get_list_of_product_prices()}\n Products on page isn't A to Z sorted"

    @allure.step("Checking that product on page is high to low sorted")
    def check_high_to_low_products_sort(self):
        assert ProductSort.high_to_low_sort(self.products.get_list_of_product_prices())



    # Working with sort selector
    @property
    def product_sort(self):
        return self.find(Locators.product_sort)

    def sort_is_displayed(self):
        expect(self.product_sort).to_be_visible()

    @allure.step("Click on sort button")
    def click_sort(self):
        self.product_sort.click()

    @allure.step("Select A to Z sort")
    def select_a_to_z_sort(self):
        self.product_sort.select_option(Locators.az_sort_selector)

    @allure.step("Select Z to A sort")
    def select_z_to_a_sort(self):
        self.product_sort.select_option(Locators.za_sort_selector)

    @allure.step("Select low to high sort")
    def select_low_to_high_sort(self):
        self.product_sort.select_option(Locators.low_to_high_sort_selector)

    @allure.step("Select high to low sort")
    def select_high_to_low_sort(self):
        self.product_sort.select_option(Locators.high_to_low_sort_selector)


    # Working with RandomItems
    @cached_property
    def get_random_times_for_add_iteration(self):
        return RandomItems.get_random_count(self.products.get_product_add_btn_count)

    @allure.step("Select one random item from page and add it to cart")
    def add_one_random_product_to_cart(self, list_of_prod: list):
        list_of_prod.append(RandomItems.select_one_random_item(self.products.get_product_add_btn_count,
                                                               self.products.click_button_add_to_card_product_by_index))
        print(list_of_prod)

    def add_random_products_to_cart(self, list_of_prod: list):
        action = partial(self.add_one_random_product_to_cart, list_of_prod)
        return RandomItems.repeat_random_amount_once_each(self.get_random_times_for_add_iteration, action)

    @cached_property
    def get_random_times_for_remove_iteration(self):
        return RandomItems.get_random_count(self.get_random_times_for_add_iteration)

    @allure.step("Select one random item from page and remove it from cart")
    def remove_one_random_product_from_cart(self, list_of_prod: list):
        list_of_prod.remove(RandomItems.select_one_random_item(
            self.products.get_product_remove_from_cart_btn_count,
            self.products.click_button_remove_from_cart_product_by_index))
        print(list_of_prod)

    def remove_random_products_from_cart(self, list_of_prod: list):
        action = partial(self.remove_one_random_product_from_cart, list_of_prod)
        return RandomItems.repeat_random_amount_once_each(self.get_random_times_for_remove_iteration, action)

    def click_on_random_product_on_page(self):
        index = (RandomItems.get_random_count(self.products.get_product_item_count()) - 1)
        self.products.click_on_selected_product(index)

    # Social media and terms elements
    @property
    def footer(self):
        return FooterComponents(self.page)