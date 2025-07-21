from pages.base_page import BasePage
from pages.locators.components.navigation_component_locators import NavigationComponentLocators as Locators



class BackAndContinue(BasePage):

    @property
    def back_btn(self):
        return self.find(Locators.back_btn)

    @property
    def continue_btn(self):
        return self.find(Locators.continue_btn)