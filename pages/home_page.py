from playwright.sync_api import Page, expect, Locator
from playwright.sync_api import sync_playwright

from pages.base_page import BasePage
from pages.locators.home_page_locators import HomePageLocators as Locators
from pages.parameters.home_page_parametrs import HomePageParameters as Parameters


class HomePage(BasePage):
    base_url = Parameters.base_url
    page_url = Parameters.page_url

    def checking_the_main_page_logo(self):
        main_page_logo = self.find(Locators.main_page_logo)
        expect(main_page_logo).to_be_visible()
        expect(main_page_logo).to_have_text(Parameters.home_page_header)

    def checking_login_text_field(self):
        username_field = self.find(Locators.username_field)
        expect(username_field).to_be_visible()
        expect(username_field).to_have_attribute('placeholder', 'Username')

    def checking_password_text_field(self):
        password_field = self.find(Locators.password_field)
        expect(password_field).to_be_visible()
        expect(password_field).to_have_attribute('placeholder', 'Password')

    def checking_header_of_list_of_users(self):
        header_of_login_field = self.find(Locators.header_of_login_field)
        expect(header_of_login_field).to_be_visible()
        expect(header_of_login_field).to_have_text(Parameters.username_header)

    def __list_of_something(self, locator):
        locator_of_something = self.find(locator)
        text_of_something = locator_of_something.inner_text()
        list_of_text = [line.strip() for line in text_of_something.splitlines() if line.strip()]
        list_of_something_text = list_of_text[1:]
        return list_of_something_text

    def checking_list_of_users(self):
        list_of_logins = self.__list_of_something(Locators.list_of_login_field)
        assert list_of_logins == Parameters.expected_list_of_users

    def checking_header_of_list_of_password(self):
        header_of_password_field = self.find(Locators.header_of_password_field)
        expect(header_of_password_field).to_be_visible()
        expect(header_of_password_field).to_have_text(Parameters.password_header)

    def checking_list_of_password(self):
        list_of_passwords = self.__list_of_something(Locators.list_of_password_field)
        assert list_of_passwords == Parameters.expected_password

    def checking_empty_error(self):
        error_empty_field = self.find(Locators.error_empty_field)
        error_field = self.find(Locators.error_field)
        expect(error_empty_field).to_be_visible()
        expect(error_empty_field).to_contain_text('')
        expect(error_empty_field).to_have_css('background-color', Parameters.empty_error_color)
        expect(error_field).to_have_count(0)

    def checking_error_of_empty_username(self):
        error_field = self.find(Locators.error_field)
        error_icon = self.find(Locators.error_icon)
        expect(error_field).to_be_visible()
        expect(error_field).to_contain_text(Parameters.empty_username_error_text)
        expect(error_field).to_have_css('background-color', Parameters.error_color)
        expect(error_icon).to_have_count(2)
        self.expect_visible(error_icon)

    def checking_error_of_empty_password(self):
        error_field = self.find(Locators.error_field)
        error_icon = self.find(Locators.error_icon)
        expect(error_field).to_be_visible()
        expect(error_field).to_contain_text(Parameters.empty_password_error_text)
        expect(error_field).to_have_css('background-color', Parameters.error_color)
        expect(error_icon).to_have_count(2)
        self.expect_visible(error_icon)

    def checking_error_of_invalid_credentials(self):
        error_field = self.find(Locators.error_field)
        error_icon = self.find(Locators.error_icon)
        expect(error_field).to_be_visible()
        expect(error_field).to_contain_text(Parameters.invalid_credentials_text)
        expect(error_field).to_have_css('background-color', Parameters.error_color)
        expect(error_icon).to_have_count(2)
        self.expect_visible(error_icon)

    def checking_username_is_written(self, username):
        username_field = self.find(Locators.username_field)
        expect(username_field).to_be_visible()
        expect(username_field).to_have_attribute('value', username)

    def checking_password_is_written(self, password):
        password_field = self.find(Locators.password_field)
        expect(password_field).to_be_visible()
        expect(password_field).to_have_attribute('value', password)

    def click_login_button(self):
        self.find(Locators.login_button).click()

    def enter_username(self, username):
        username_field = self.find(Locators.username_field)
        username_field.click()
        username_field.fill(username)

    def enter_password(self, password):
        password_field = self.find(Locators.password_field)
        password_field.click()
        password_field.fill(password)

    def checking_new_page_after_login(self):
        expect(self.page).to_have_url(Parameters.new_page_url)