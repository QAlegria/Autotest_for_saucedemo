from config import setting
from pages.parameters.check_out_first_page_parameters import CheckOutFirstPageParameters


def test_fill_checkout_form(inventory_page, cart_page, checkout_first_page, first_name, last_name, postal_code):
    inventory_page.page_components.click_shopping_cart()
    cart_page.click_checkout_btn()
    checkout_first_page.fill_first_name(first_name)
    checkout_first_page.check_first_name_field_is_filled_with_text(first_name)
    checkout_first_page.fill_last_name(last_name)
    checkout_first_page.check_last_name_field_is_filled_with_text(last_name)
    checkout_first_page.fill_postal_code(postal_code)
    checkout_first_page.check_postal_code_field_is_filled_with_text(postal_code)
    checkout_first_page.click_continue_btn()
    checkout_first_page.check_url_is(setting.CHECK_OUT_SECOND_PAGE_URL)

def test_checkout_form_errors(inventory_page, cart_page, checkout_first_page, first_name, last_name, postal_code, ):
    inventory_page.page_components.click_shopping_cart()
    cart_page.click_checkout_btn()
    checkout_first_page.click_continue_btn()
    checkout_first_page.error_of_empty_first_name(CheckOutFirstPageParameters.empty_first_name_err_txt)
    checkout_first_page.fill_first_name(first_name)
    checkout_first_page.check_first_name_field_is_filled_with_text(first_name)
    checkout_first_page.click_continue_btn()
    checkout_first_page.error_of_empty_last_name_has_text(CheckOutFirstPageParameters.empty_last_name_err_txt)
    checkout_first_page.fill_last_name(last_name)
    checkout_first_page.check_last_name_field_is_filled_with_text(last_name)
    checkout_first_page.click_continue_btn()
    checkout_first_page.error_of_empty_postal_code_has_text(CheckOutFirstPageParameters.empty_postal_code_err_txt)
    checkout_first_page.fill_postal_code(postal_code)
    checkout_first_page.check_postal_code_field_is_filled_with_text(postal_code)
    checkout_first_page.click_continue_btn()
    checkout_first_page.check_url_is(setting.CHECK_OUT_SECOND_PAGE_URL)