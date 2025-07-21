from time import sleep

from config import setting
from tests.components.test_footer import check_footer_on_page
from tests.components.test_left_menu import check_left_menu_with_buttons_is_displayed_on


def test_check_out_first_page_default_state(check_out_first_page):
    check_left_menu_with_buttons_is_displayed_on(check_out_first_page)
    check_out_first_page.page_components.check_header_of_product_title_has_text('Checkout: Your Information')
    check_out_first_page.page_components.shopping_cart_icon_is_displayed()
    check_out_first_page.page_components.check_product_counter_icon_is_not_displayed()
    check_out_first_page.check_first_name_field_is_displayed()
    check_out_first_page.check_last_name_field_is_displayed()
    check_out_first_page.check_postal_code_field_is_displayed()
    check_out_first_page.continue_btn_has_text('Continue')
    check_out_first_page.cancel_btn_has_text('Cancel')
    check_footer_on_page(check_out_first_page)


def test_fill_checkout_form(check_out_first_page, first_name, last_name, postal_code):
    check_out_first_page.fill_first_name(first_name)
    check_out_first_page.check_first_name_field_is_filled_with_text(first_name)
    check_out_first_page.fill_last_name(last_name)
    check_out_first_page.check_last_name_field_is_filled_with_text(last_name)
    check_out_first_page.fill_postal_code(postal_code)
    check_out_first_page.check_postal_code_field_is_filled_with_text(postal_code)
    check_out_first_page.click_continue_btn()
    check_out_first_page.check_url_is(setting.CHECK_OUT_SECOND_PAGE_URL)

def test_checkout_form_errors(check_out_first_page, first_name, last_name, postal_code):
    check_out_first_page.click_continue_btn()
    check_out_first_page.error_of_empty_last_name_has_text('Error: First Name is required')
    check_out_first_page.fill_first_name(first_name)
    check_out_first_page.check_first_name_field_is_filled_with_text(first_name)
    check_out_first_page.click_continue_btn()
    check_out_first_page.error_of_empty_last_name_has_text('Error: Last Name is required')
    check_out_first_page.fill_last_name(last_name)
    check_out_first_page.check_last_name_field_is_filled_with_text(last_name)
    check_out_first_page.click_continue_btn()
    check_out_first_page.error_of_empty_last_name_has_text('Error: Postal Code is required')
    check_out_first_page.fill_postal_code(postal_code)
    check_out_first_page.check_postal_code_field_is_filled_with_text(postal_code)
    check_out_first_page.click_continue_btn()
    check_out_first_page.check_url_is(setting.CHECK_OUT_SECOND_PAGE_URL)