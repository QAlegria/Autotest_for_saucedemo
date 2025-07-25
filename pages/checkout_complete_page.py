from config import setting
from pages.base_page import BasePage
from pages.components.cart_and_page_component import ExtendedPageComponents
from pages.components.footer_component import FooterComponents
from pages.locators.checkout_complete_page_locators import CompleteCheckOutPageLocators as Locators


class CheckOutCompletePage(BasePage):

    # Working with logo, cart_icon, title
    @property
    def page_components(self):
        return ExtendedPageComponents(self.page)

    # Working with complete container
    @property
    def complete_image_element(self):
        return self.find(Locators.complete_image)

    @property
    def complete_header_element(self):
        return self.find(Locators.complete_header)

    def complete_header_has_text(self, text):
        self.check_visibility_and_text(self.complete_header_element, text)

    @property
    def complete_text_element(self):
        return self.find(Locators.complete_text)

    def complete_text_has_text(self, text):
        self.check_visibility_and_text(self.complete_text_element, text)

    # Working with navigation
    @property
    def back_home_element(self):
        return self.find(Locators.back_home)

    def back_home_btn_has_text(self, text):
        self.check_visibility_and_text(self.back_home_element, text)

    def click_back_home_btn(self):
        self.back_home_element.click()



    # Social media and terms elements
    @property
    def footer(self):
        return FooterComponents(self.page)