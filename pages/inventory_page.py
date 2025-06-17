from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.parameters.inventory_page_parameters import InventoryPageParameters as Parameters
from pages.locators.inventory_page_locators import InventoryPageLocators as Locators
from utils.image_checker import ImageChecker

class InventoryPage(BasePage):

    def checking_the_inventory_page_logo(self):
        inventory_page_logo = self.find(Locators.inventory_page_logo)
        expect(inventory_page_logo).to_be_visible()
        expect(inventory_page_logo).to_have_text(Parameters.inventory_page_header)

    def checking_correct_image(self):
        shopping_cart = self.find(Locators.shopping_cart)
        expect(shopping_cart).to_be_visible()
        ImageChecker.checking_image_link_of_element(shopping_cart, Parameters.shopping_card_image_name)