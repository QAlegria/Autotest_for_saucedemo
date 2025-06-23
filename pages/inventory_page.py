from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.parameters.inventory_page_parameters import InventoryPageParameters as Parameters
from pages.locators.inventory_page_locators import InventoryPageLocators as Locators
from utils.image_checker import ImageChecker
from utils.json_worker import JsonWorker
from config import setting

class InventoryPage(BasePage):

    def checking_the_inventory_page_logo(self):
        inventory_page_logo = self.find(Locators.inventory_page_logo)
        expect(inventory_page_logo).to_be_visible()
        expect(inventory_page_logo).to_have_text(Parameters.inventory_page_header)

    def checking_shopping_cart_image(self):
        shopping_cart = self.find(Locators.shopping_cart)
        expect(shopping_cart).to_be_visible()
        ImageChecker.checking_image_link_of_element(shopping_cart, Parameters.shopping_card_image_name)

    def checking_left_slide_button(self):
        left_slide_button = self.find(Locators.left_slide_button)
        expect(left_slide_button).to_be_visible()

    def click_left_slide_button(self):
        left_slide_button = self.find(Locators.left_slide_button)
        left_slide_button.click()

    def click_close_button(self):
        button_to_close_left_menu = self.find(Locators.button_to_close_left_menu)
        button_to_close_left_menu.click()

    def checking_left_menu(self):
        button_to_main_menu = self.find(Locators.button_to_main_menu)
        button_about = self.find(Locators.button_about)
        logout_button = self.find(Locators.logout_button)
        reset_button = self.find(Locators.reset_button)
        expect(button_to_main_menu).to_be_visible()
        expect(button_about).to_be_visible()
        expect(logout_button).to_be_visible()
        expect(reset_button).to_be_visible()

    def checking_filter_is_exist(self):
        product_filter = self.find(Locators.product_filter)
        expect(product_filter).to_be_visible()

    def checking_header_of_product_title(self):
        header_of_product_title = self.find(Locators.header_of_product_title)
        expect(header_of_product_title).to_be_visible()
        expect(header_of_product_title).to_have_text(Parameters.header_of_product_title_text)

    def checking_first_product_card_image(self):
        product_image = self.find(Locators.product_image).nth(0)
        expect(product_image).to_be_visible()
        product_name = product_image.get_attribute('alt')
        product_image_url = product_image.get_attribute('src')
        product_json_filter = JsonWorker()
        product_json_filter.open_file(setting.JSON_DIR)
        product_items_for_image = product_json_filter.get_product_by_conditions(name = product_name, image_url = product_image_url)
        assert product_items_for_image

    def checking_first_product_card_name_and_description(self):
        product_name_header = self.find(Locators.product_name_header).nth(0)
        product_description = self.find(Locators.product_description).nth(0)
        expect(product_name_header).to_be_visible()
        expect(product_description).to_be_visible()
        header_name = product_name_header.inner_text()
        description = product_description.inner_text()
        product_json_filter = JsonWorker()
        product_json_filter.open_file(setting.JSON_DIR)
        product_items_for_name = product_json_filter.get_product_by_conditions(name=header_name, description=description)
        assert product_items_for_name