import allure
from playwright.sync_api import expect, BrowserContext
from pages.base_page import BasePage
from pages.components.cart_and_page_components import ExtendedPageComponents
from pages.components.footer_components import FooterComponents
from pages.components.left_menu_component import LeftMenu
from pages.components.product_components import CartProducts
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
    def description_label(self):
        return self.find(Locators.description_label)

    def description_label_has_text(self, text):
        self.check_visibility_and_text(self.description_label, text)

    @property
    def cart_list(self):
        return self.find(Locators.list_of_cart_products)

    def check_cart_list_is_empty(self):
        expect(self.products.product_item).to_have_count(0)


    # Working wih product cards
    @property
    def products(self):
        return CartProducts(self.page, self.network)


    # Working with navigation
    @property
    def continue_shopping_btn(self):
        return self.find(Locators.btn_continue_shop)

    def continue_shopping_btn_has_text(self, text):
        self.check_visibility_and_text(self.continue_shopping_btn, text)

    def click_continue_shopping_btn(self):
        self.continue_shopping_btn.click()

    @property
    def checkout_btn(self):
        return self.find(Locators.btn_checkout)

    def checkout_btn_has_text(self, text):
        self.check_visibility_and_text(self.checkout_btn, text)

    def click_checkout_btn(self):
        self.checkout_btn.click()


    # Social media and terms elements
    @property
    def footer(self):
        return FooterComponents(self.page)
