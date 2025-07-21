import allure
from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.components.cart_and_page_component import ExtendedPageComponents
from pages.components.error_component import ErrorComponents
from pages.components.footer_component import FooterComponents
from pages.components.left_menu_component import LeftMenu
from pages.components.navigation_component import BackAndContinue
from pages.locators.check_out_first_page_locators import CheckOutFirstPageLocators as Locators



class CheckOutFirstPage(BasePage):

    # Working with logo, cart_icon, title
    @property
    def page_components(self):
        return ExtendedPageComponents(self.page)

    # Working with left menu
    @property
    def left_menu(self):
        return LeftMenu(self.page)

    # Working wih info panel
    @property
    def first_name_field_element(self):
        return self.find(Locators.first_name_field)

    def check_first_name_field_is_displayed(self):
        expect(self.first_name_field_element).to_be_visible()

    def fill_first_name(self, text):
        self.first_name_field_element.fill(text)

    def check_first_name_field_is_filled_with_text(self, text):
        self.check_visibility_and_attribute(self.first_name_field_element, 'value', text)

    @property
    def last_name_field_element(self):
        return self.find(Locators.last_name_field)

    def check_last_name_field_is_displayed(self):
        expect(self.last_name_field_element).to_be_visible()

    def fill_last_name(self, text):
        self.last_name_field_element.fill(text)

    def check_last_name_field_is_filled_with_text(self, text):
        self.check_visibility_and_attribute(self.last_name_field_element, 'value', text)


    @property
    def postal_code_field_element(self):
        return self.find(Locators.postal_code_field)

    def check_postal_code_field_is_displayed(self):
        expect(self.postal_code_field_element).to_be_visible()

    def fill_postal_code(self, text):
        self.postal_code_field_element.fill(text)

    def check_postal_code_field_is_filled_with_text(self, text):
        self.check_visibility_and_attribute(self.postal_code_field_element, 'value', text)


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
    def continue_btn(self):
        return self.navigation.continue_btn

    def continue_btn_has_text(self, text):
        self.check_visibility_and_attribute(self.continue_btn, 'value', text)

    def click_continue_btn(self):
        self.continue_btn.click()


    # Working with errors
    @property
    def error(self):
        return ErrorComponents(self.page)

    @allure.step("Checking empty first name error")
    def error_of_empty_first_name(self, text):
        self.error.checking_error_of_empty_field(text)

    @allure.step("Checking empty last name error text")
    def error_of_empty_last_name_has_text(self, text):
        self.error.checking_error_of_empty_field(text)

    @allure.step("Checking empty post code error text")
    def error_of_empty_postal_code_has_text(self, text):
        self.error.checking_error_of_empty_field(text)

    def error_icons_is_displayed(self):
        self.error.error_icons_is_displayed_and_have_count(3)



    # Social media and terms elements
    @property
    def footer(self):
        return FooterComponents(self.page)
