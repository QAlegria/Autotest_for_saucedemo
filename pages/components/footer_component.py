import allure

from config import setting
from pages.base_page import BasePage
from pages.locators.components.footer_locators import FooterLocators as Locators


class FooterComponents(BasePage):
    # Social media and terms elements
    @property
    def twitter_element(self):
        return self.find(Locators.twitter_logo_link)

    def twitter_is_displayed(self):
        self.check_visibility_and_attribute(self.twitter_element, 'href', setting.TWITTER_LINK)

    @allure.step("Click to twitter logo and check is it opened")
    def click_and_check_twitter_is_opened(self):
        twitter_page = self.open_new_tab_with_click(self.twitter_element)
        twitter_page.wait_for_url(setting.X_TWITTER_LINK)


    @property
    def facebook_element(self):
        return self.find(Locators.facebook_logo_link)

    def facebook_is_displayed(self):
        self.check_visibility_and_attribute(self.facebook_element, 'href', setting.FACEBOOK_LINK)

    @allure.step("Click to facebook logo and check is it opened")
    def click_and_check_facebook_is_opened(self):
        facebook_page = self.open_new_tab_with_click(self.facebook_element)
        facebook_page.wait_for_url(setting.FACEBOOK_LINK)

    @property
    def linkedin_element(self):
        return self.find(Locators.linkedin_logo_link)

    def linkedin_is_displayed(self):
        self.check_visibility_and_attribute(self.linkedin_element, 'href', setting.LINKEDIN_LINK)

    @allure.step("Click to linkedin logo and check is it opened")
    def click_and_check_linkedin_is_opened(self):
        linkedin_page = self.open_new_tab_with_click(self.linkedin_element)
        linkedin_page.wait_for_url(setting.LINKEDIN_LINK)


    @property
    def terms_footer(self):
        return self.find(Locators.terms_footer)

    def terms_footer_is_displayed(self):
        self.check_visibility_and_text(self.terms_footer, setting.TERMS_FOOTER_TEXT)