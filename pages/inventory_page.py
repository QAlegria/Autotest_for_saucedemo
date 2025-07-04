from functools import cached_property

from playwright.sync_api import expect, BrowserContext
from pages.base_page import BasePage
from pages.parameters.inventory_page_parameters import InventoryPageParameters as Parameters
from pages.locators.inventory_page_locators import InventoryPageLocators as Locators
from utils.json_worker import JsonWorker
from config import setting
from utils.helpers import PriceHelper, ProductSort, RandomItems


class InventoryPage(BasePage):

    @property
    def inventory_page_logo(self):
        return self.find(Locators.inventory_page_logo)

    def inventory_page_logo_is_displayed_and_has_text(self, text):
        self.check_visibility_and_text(self.inventory_page_logo, text)


    # Working with shopping cart
    @property
    def shopping_cart_image(self):
        return self.find(Locators.shopping_cart)

    def shopping_cart_image_is_displayed(self):
        expect(self.shopping_cart_image).to_be_visible()

    def shopping_cart_image_is_on_page(self):
        self.check_element_image_link(self.shopping_cart_image,Parameters.shopping_card_image_name)

    @property
    def shopping_cart_counter(self):
        return self.find(Locators.shopping_cart_counter)

    def check_product_counter_icon_is(self, count):
        self.check_visibility_and_text(self.shopping_cart_counter, str(count))

    def check_product_counter_icon_is_equals_random_selected_products(self):
        self.check_visibility_and_text(self.shopping_cart_counter, str(self.get_random_times_for_add_iteration))

    def check_product_counter_icon_is_equals_selected_minus_removed_products(self):
        if self.get_random_times_for_add_iteration - self.get_random_times_for_remove_iteration == 0:
            self.check_product_counter_icon_is_not_displayed()
        else:
            self.check_visibility_and_text(self.shopping_cart_counter, str(self.get_random_times_for_add_iteration-self.get_random_times_for_remove_iteration))

    def check_product_counter_icon_is_not_displayed(self):
        expect(self.shopping_cart_counter).not_to_be_attached()



    # Working with left menu
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


    def sort_is_displayed(self):
        expect(self.product_sort).to_be_visible()

    def click_sort(self):
        self.product_sort.click()

    @property
    def header_of_product_title(self):
        return self.find(Locators.header_of_product_title)

    def header_of_product_title_has_text(self, text):
        self.check_visibility_and_text(self.header_of_product_title, text)



    # Working with product cards

    @property
    def all_product_names(self):
        return self.find(Locators.product_name_header)

    def get_list_of_product_names(self):
        return self.all_product_names.all_inner_texts()

    def check_products_is_a_to_z_sorted(self):
        assert ProductSort.a_to_z_sort(self.get_list_of_product_names()), f"{self.get_list_of_product_names()}\n Products on page isn't A to Z sorted"

    def check_products_is_z_to_a_sorted(self):
        assert ProductSort.z_to_a_sort(self.get_list_of_product_names()), f"{self.get_list_of_product_names()}\n Products on page isn't Z to A sorted"

    @property
    def all_product_prices(self):
        return self.find(Locators.product_price)

    def get_list_of_product_prices(self):
        return PriceHelper.get_float_prices(self.all_product_prices.all_inner_texts())

    def check_low_to_high_products_sort(self):
        assert ProductSort.low_to_high_sort(self.get_list_of_product_prices()), f"{self.get_list_of_product_prices()}\n Products on page isn't A to Z sorted"

    def check_high_to_low_products_sort(self):
        assert ProductSort.high_to_low_sort(self.get_list_of_product_prices())



    # Working with sort selector
    @property
    def product_sort(self):
        return self.find(Locators.product_sort)

    def click_product_sort(self):
        self.product_sort.click()

    def select_a_to_z_sort(self):
        self.product_sort.select_option(Locators.az_sort_selector)

    def select_z_to_a_sort(self):
        self.product_sort.select_option(Locators.za_sort_selector)

    def select_low_to_high_sort(self):
        self.product_sort.select_option(Locators.low_to_high_sort_selector)

    def select_high_to_low_sort(self):
        self.product_sort.select_option(Locators.high_to_low_sort_selector)



    # Searching product elements by index:

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
        assert product_items_for_name,(f"Mismatch between product on page\n {self.get_product_name_by_index(index)}\n"
                                       f"{self.get_product_description_by_index(index)}\n ,"
                                       f"{self.get_product_image_url_by_index(index)}\n ,"
                                       f"{self.get_product_price_by_index(index)}\n ,"
                                       f"{self.get_product_currency_by_index(index)}\n and product in JSON")

    def check_was_request_of_product_image_called_by_index(self, index):
        url = self.get_product_image_url_by_index(index)
        assert self.network.was_url_requested(url=url), 'The specified request was not requested'



    # Button add to cart
    @property
    def get_product_add_btn_count(self) -> int:
        return self.find(Locators.button_add_to_cart).count()

    def add_to_cart_element(self, index):
        return self.find_by_index(Locators.button_add_to_cart, index)

    def button_add_to_cart_by_index_is_displayed(self, index):
        self.check_visibility_and_text(self.add_to_cart_element(index), Parameters.add_to_cart)

    def click_button_add_to_card_product_by_index(self, index):
        self.add_to_cart_element(index).click()

    # Button remove from cart
    @property
    def get_product_remove_from_cart_btn_count(self) -> int:
        return self.find(Locators.button_to_remove_from_cart).count()

    def remove_from_cart_element(self, index):
        return self.find_by_index(Locators.button_to_remove_from_cart, index)

    def button_remove_from_cart_by_index_is_displayed(self, index):
        self.check_visibility_and_text(self.remove_from_cart_element(index), Parameters.remove_from_cart)

    def click_button_remove_from_cart_product_by_index(self, index):
        self.remove_from_cart_element(index).click()

    # Working with RandomItems
    @cached_property
    def get_random_times_for_add_iteration(self):
        return RandomItems.get_random_count(self.get_product_add_btn_count)

    def add_one_random_product_to_cart(self):
        RandomItems.select_one_random_item(self.get_product_add_btn_count, self.click_button_add_to_card_product_by_index)

    def add_random_products_to_cart(self):
        return RandomItems.repeat_random_amount_once_each(self.get_random_times_for_add_iteration, self.add_one_random_product_to_cart)

    @cached_property
    def get_random_times_for_remove_iteration(self):
        return RandomItems.get_random_count(self.get_random_times_for_add_iteration)

    def remove_one_random_product_from_cart(self):
        RandomItems.select_one_random_item(self.get_product_remove_from_cart_btn_count, self.click_button_remove_from_cart_product_by_index)

    def remove_random_products_from_cart(self):
        return RandomItems.repeat_random_amount_once_each(self.get_random_times_for_remove_iteration, self.remove_one_random_product_from_cart)



    # Social media and terms elements
    @property
    def twitter_element(self):
        return self.find(Locators.twitter_logo_link)

    def twitter_is_displayed(self):
        self.check_visibility_and_attribute(self.twitter_element, 'href', setting.TWITTER_LINK)

    def click_and_check_twitter_is_opened(self):
        twitter_page = self.open_new_tab_with_click(self.twitter_element)
        twitter_page.wait_for_url(setting.X_TWITTER_LINK)


    @property
    def facebook_element(self):
        return self.find(Locators.facebook_logo_link)

    def facebook_is_displayed(self):
        self.check_visibility_and_attribute(self.facebook_element, 'href', setting.FACEBOOK_LINK)

    def click_and_check_facebook_is_opened(self):
        facebook_page = self.open_new_tab_with_click(self.facebook_element)
        facebook_page.wait_for_url(setting.FACEBOOK_LINK)

    @property
    def linkedin_element(self):
        return self.find(Locators.linkedin_logo_link)

    def linkedin_is_displayed(self):
        self.check_visibility_and_attribute(self.linkedin_element, 'href', setting.LINKEDIN_LINK)

    def click_and_check_linkedin_is_opened(self):
        linkedin_page = self.open_new_tab_with_click(self.linkedin_element)
        linkedin_page.wait_for_url(setting.LINKEDIN_LINK)


    @property
    def terms_footer(self):
        return self.find(Locators.terms_footer)

    def terms_footer_is_displayed(self):
        self.check_visibility_and_text(self.terms_footer, Parameters.terms_footer_text)


