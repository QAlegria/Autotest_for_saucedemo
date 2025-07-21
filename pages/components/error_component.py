import allure
from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.locators.components.error_component_locators import ErrorComponentLocators as Locators
from pages.parameters.components.error_component_parameters import ErrorComponentParameters as Parameters


class ErrorComponents(BasePage):

    @property
    def empty_error_field(self):
        return self.find(Locators.empty_error_field)

    @property
    def not_empty_error_field(self):
        return self.find(Locators.not_empty_error_field)

    def empty_error_field_is_displayed(self):
        self.check_visibility_and_text(self.empty_error_field, '')
        expect(self.empty_error_field).to_have_css('background-color', Parameters.empty_error_color)
        expect(self.not_empty_error_field).to_have_count(0)

    @allure.step("Checking empty field error")
    def checking_error_of_empty_field(self, text):
        self.check_visibility_and_text(self.not_empty_error_field, text)
        expect(self.not_empty_error_field).to_have_css('background-color', Parameters.error_color)

    @property
    def error_icons(self):
        return self.find(Locators.error_icon)

    def error_icons_is_displayed_and_have_count(self, count):
        expect(self.error_icons).to_have_count(count)
        self.check_visibility_list_of_elements(self.error_icons)

    @allure.step("Checking error text")
    def error_description_has_text(self, text):
        self.check_visibility_and_text(self.not_empty_error_field, text)
        expect(self.not_empty_error_field).to_have_css('background-color', Parameters.error_color)

