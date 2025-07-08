import allure

from pages.base_page import BasePage
from playwright.sync_api import expect
from pages.locators.components.left_menu_locators import LeftMenuLocators as Locators



class LeftMenu(BasePage):

    # Working with left menu
    @property
    def left_menu_button(self):
        return self.find(Locators.left_menu_button)

    def left_menu_button_is_displayed(self):
        expect(self.left_menu_button).to_be_visible()

    @allure.step("Click on left menu button")
    def click_left_menu_button(self):
        self.left_menu_button.click()

    @property
    def button_to_close_left_menu(self):
        return self.find(Locators.button_to_close_left_menu)

    @allure.step("Click on close left menu button")
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

    @allure.step("Click on main menu button")
    def click_button_to_main_menu(self):
        self.button_to_main_menu.click()

    def button_about_is_displayed(self):
        expect(self.button_about).to_be_visible()

    @allure.step("Click on about button")
    def click_button_about(self):
        self.button_about.click()

    def logout_button_is_displayed(self):
        expect(self.logout_button).to_be_visible()

    @allure.step("Click on logout button")
    def click_logout_button(self):
        self.logout_button.click()

    def reset_button_is_displayed(self):
        expect(self.reset_button).to_be_visible()

    @allure.step("Click on reset button")
    def click_reset_button(self):
        self.reset_button.click()