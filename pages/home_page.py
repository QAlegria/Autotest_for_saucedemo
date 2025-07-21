import allure
from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.components.error_component import ErrorComponents
from pages.locators.home_page_locators import HomePageLocators as Locators
from pages.parameters.home_page_parameters import HomePageParameters as Parameters
from utils.helpers import LoginDivideHelper
from config import setting


class HomePage(BasePage):
    base_url = Parameters.base_url
    page_url = setting.HOME_PAGE_URL

    @property
    def main_page_logo(self):
        return self.find(Locators.main_page_logo)

    def main_page_logo_has_text(self, text):
        self.check_visibility_and_text(self.main_page_logo, text)

    # Working with input fields

    @property
    def username_text_field(self):
        return self.find(Locators.username_field)

    def username_text_field_is_displayed(self):
        self.check_visibility_and_attribute(self.username_text_field, 'placeholder', 'Username')

    def username_text_field_has_value(self, username):
        self.check_visibility_and_attribute(self.username_text_field,'value', username)

    @allure.step("Filling username")
    def enter_username(self, username):
        self.username_text_field.click()
        self.username_text_field.fill(username)

    @property
    def password_text_field(self):
        return self.find(Locators.password_field)

    def password_text_field_is_displayed(self):
        self.check_visibility_and_attribute(self.password_text_field,'placeholder', 'Password')

    def password_text_field_has_value(self, password):
        self.check_visibility_and_attribute(self.password_text_field,'value', password)

    @allure.step("Filling password")
    def enter_password(self, password):
        self.password_text_field.click()
        self.password_text_field.fill(password)


    @property
    def header_of_list_of_users(self):
        return self.find(Locators.header_of_accepted_logins_list)

    def header_of_list_of_users_has_text(self, text):
        self.check_visibility_and_text(self.header_of_list_of_users, text)

    @property
    def element_list_of_accepted_login(self):
        return self.find(Locators.list_of_accepted_login)

    @allure.step("Compare list of logins with expected list")
    def list_of_users_match_with(self, expected_list):
        list_of_logins = LoginDivideHelper.text_to_divide_from_page(self.element_list_of_accepted_login)
        assert list_of_logins == expected_list, "list_of_logins is not matching with expected_list_of_logins"

    @property
    def header_of_accepted_list_of_password(self):
        return self.find(Locators.header_of_accepted_password_list)

    def header_of_accepted_list_of_password_has_text(self, text):
        self.check_visibility_and_text(self.header_of_accepted_list_of_password, text)

    @property
    def element_list_of_accepted_pass(self):
        return self.find(Locators.list_of_accepted_password)

    @allure.step("Compare list of password with expected list")
    def list_of_password_match_with(self, expected_list):
        list_of_passwords = LoginDivideHelper.text_to_divide_from_page(self.element_list_of_accepted_pass)
        assert list_of_passwords == expected_list, "list_of_password is not matching with expected_list_of_passwords"

    # Working with errors
    @property
    def error(self):
        return ErrorComponents(self.page)

    @allure.step("Checking empty username error")
    def checking_error_of_empty_username(self, text):
        self.error.checking_error_of_empty_field(text)

    def error_icons_is_displayed(self):
        self.error.error_icons_is_displayed_and_have_count(2)

    @allure.step("Checking error text")
    def error_of_empty_password_has_text(self, text):
        self.error.checking_error_of_empty_field(text)

    @allure.step("Checking error text")
    def error_of_invalid_credentials_has_text(self, text):
        self.error.error_description_has_text(text)


    @allure.step("Clicking on login button")
    def click_login_button(self):
        self.find(Locators.login_button).click()


    @allure.step("Checking Inventory page after login")
    def new_page_after_login_has_url(self, url):
        self.check_url_is(url)