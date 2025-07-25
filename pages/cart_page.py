import allure
from playwright.sync_api import expect, BrowserContext

from config import setting
from pages.base_page import BasePage
from pages.components.cart_and_page_component import ExtendedPageComponents
from pages.components.footer_component import FooterComponents
from pages.components.left_menu_component import LeftMenu
from pages.components.navigation_component import BackAndContinue
from pages.components.product_component import CartProducts
from pages.parameters.cart_page_parameters import CartPageParameters as Parameters
from pages.locators.cart_page_locators import CartPageLocators as Locators
from utils.json_worker import JsonWorker
from utils.helpers import PriceHelper, ProductSort, RandomItems

class CartPage(BasePage):

    # Working with logo, cart_icon, title
    @property
    def page_components(self):
        return ExtendedPageComponents(self.page)

    # Working with left menu
    @property
    def left_menu(self):
        return LeftMenu(self.page)


    # Working with product list

    @property
    def cart_list(self):
        return self.find(Locators.list_of_cart_products)

    def check_cart_list_is_empty(self):
        expect(self.products.description.product_item).to_have_count(0)


    # Working wih product cards
    @property
    def products(self):
        return CartProducts(self.page, self.network)


    def check_prod_list_from_inventory_page_is_right(self, prod_list):
        print(self.products.description.get_list_of_product_names())
        assert self.products.description.get_list_of_product_names() == prod_list



    # Working with navigation
    @property
    def navigation(self):
        return BackAndContinue(self.page)

    @property
    def continue_shopping_btn(self):
        return self.navigation.back_btn

    def continue_shopping_btn_has_text(self, text):
        self.check_visibility_and_text(self.continue_shopping_btn, text)

    def click_continue_shopping_btn(self):
        self.continue_shopping_btn.click()

    @property
    def checkout_btn(self):
        return self.navigation.continue_btn

    def checkout_btn_has_text(self, text):
        self.check_visibility_and_text(self.checkout_btn, text)

    def click_checkout_btn(self):
        self.checkout_btn.click()

    # Social media and terms elements
    @property
    def footer(self):
        return FooterComponents(self.page)
