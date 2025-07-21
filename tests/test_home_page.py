from time import sleep
import allure
import pytest

from config import setting
from pages.parameters.home_page_parameters import HomePageParameters as Parameters


@allure.epic("SauceDemo Home Page")
@allure.feature("Default page state")
@allure.story("Default page state")
def test_main_page_default_state(main_page):
    main_page.open()
    main_page.main_page_logo_has_text(setting.LOGO)
    main_page.username_text_field_is_displayed()
    main_page.password_text_field_is_displayed()
    main_page.header_of_list_of_users_has_text(Parameters.username_header)
    main_page.list_of_users_match_with(Parameters.expected_list_of_logins)
    main_page.header_of_accepted_list_of_password_has_text(Parameters.password_header)
    main_page.list_of_password_match_with(Parameters.expected_passwords)
    main_page.error.empty_error_field_is_displayed()



def test_main_page_empty_username(main_page, wrong_username):
    main_page.open()
    main_page.click_login_button()
    main_page.checking_error_of_empty_username(Parameters.empty_username_error_text)
    main_page.error_icons_is_displayed()


def test_main_page_empty_password(main_page, standard_user):
    main_page.open()
    main_page.enter_username(standard_user)
    main_page.click_login_button()
    main_page.error_of_empty_password_has_text(Parameters.empty_password_error_text)
    main_page.error_icons_is_displayed()


# @pytest.mark.parametrize("username", "password", "expected_error_text",
#                          [
#                              pytest.param(wrong_username, valid_password, Parameters.invalid_credentials_text, id="Wrong username"),
#                              pytest.param(standard_user, invalid_password, Parameters.invalid_credentials_text, id="Invalid password"),
#                              pytest.param(locked_out_user, valid_password, Parameters.locked_out_user_error_text, id="Locked out user")])

def test_main_page_errors_while_login(main_page, wrong_username, valid_password):
    main_page.open()
    main_page.enter_username(wrong_username)
    main_page.username_text_field_has_value(wrong_username)
    main_page.enter_password(valid_password)
    main_page.password_text_field_has_value(valid_password)
    main_page.click_login_button()
    main_page.error_of_invalid_credentials_has_text(Parameters.invalid_credentials_text)
    main_page.error_icons_is_displayed()



def test_main_page_invalid_password(main_page, standard_user, invalid_password):
    main_page.open()
    main_page.enter_username(standard_user)
    main_page.username_text_field_has_value(standard_user)
    main_page.enter_password(invalid_password)
    main_page.password_text_field_has_value(invalid_password)
    main_page.click_login_button()
    main_page.error_of_invalid_credentials_has_text(Parameters.invalid_credentials_text)
    main_page.error_icons_is_displayed()


def test_main_page_locked_out_user_error(main_page, locked_out_user, valid_password):
    main_page.open()
    main_page.enter_username(locked_out_user)
    main_page.username_text_field_has_value(locked_out_user)
    main_page.enter_password(valid_password)
    main_page.password_text_field_has_value(valid_password)
    main_page.click_login_button()
    main_page.error_of_invalid_credentials_has_text(Parameters.locked_out_user_error_text)
    main_page.error_icons_is_displayed()


def test_main_page_standard_user_login(main_page, standard_user, valid_password):
    main_page.open()
    main_page.enter_username(standard_user)
    main_page.username_text_field_has_value(standard_user)
    main_page.enter_password(valid_password)
    main_page.password_text_field_has_value(valid_password)
    main_page.click_login_button()
    main_page.new_page_after_login_has_url(setting.INVENTORY_PAGE_URL)


def test_main_page_problem_user_login(main_page, problem_user, valid_password):
    main_page.open()
    main_page.enter_username(problem_user)
    main_page.username_text_field_has_value(problem_user)
    main_page.enter_password(valid_password)
    main_page.password_text_field_has_value(valid_password)
    main_page.click_login_button()
    main_page.new_page_after_login_has_url(setting.INVENTORY_PAGE_URL)


def test_main_page_performance_glitch_user_login(main_page, performance_glitch_user, valid_password):
    main_page.open()
    main_page.enter_username(performance_glitch_user)
    main_page.username_text_field_has_value(performance_glitch_user)
    main_page.enter_password(valid_password)
    main_page.password_text_field_has_value(valid_password)
    main_page.click_login_button()
    main_page.new_page_after_login_has_url(setting.INVENTORY_PAGE_URL)


def test_main_page_visual_user_login(main_page, visual_user, valid_password):
    main_page.open()
    main_page.enter_username(visual_user)
    main_page.username_text_field_has_value(visual_user)
    main_page.enter_password(valid_password)
    main_page.password_text_field_has_value(valid_password)
    main_page.click_login_button()
    main_page.new_page_after_login_has_url(setting.INVENTORY_PAGE_URL)


def test_main_page_error_user_login(main_page, error_user, valid_password):
    main_page.open()
    main_page.enter_username(error_user)
    main_page.username_text_field_has_value(error_user)
    main_page.enter_password(valid_password)
    main_page.password_text_field_has_value(valid_password)
    main_page.click_login_button()
    main_page.new_page_after_login_has_url(setting.INVENTORY_PAGE_URL)


def test_inventory_page_without_log_in(main_page):
    main_page.open()
    main_page.page.goto(setting.INVENTORY_PAGE_URL)
    main_page.check_url_is(setting.HOME_PAGE_URL)
    main_page.error_of_invalid_credentials_has_text(Parameters.inventory_page_without_login_error_text)
    main_page.error_icons_is_displayed()


def test_cart_page_without_log_in(main_page):
    main_page.open()
    main_page.page.goto(setting.CART_PAGE_URL)
    main_page.check_url_is(setting.HOME_PAGE_URL)
    main_page.error_of_invalid_credentials_has_text(Parameters.cart_page_without_login_error_text)
    main_page.error_icons_is_displayed()



