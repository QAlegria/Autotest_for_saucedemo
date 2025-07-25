import allure

from config import setting
from config.static_image_name import ImageName
from pages.parameters.check_out_first_page_parameters import CheckOutFirstPageParameters
from pages.parameters.check_out_second_page_parameters import CheckOutSecondPageParameters
from pages.parameters.checkout_complete_page import CheckOutCompletePageParameters
from pages.parameters.home_page_parameters import HomePageParameters as HomePageParameters
from pages.parameters.inventory_page_parameters import InventoryPageParameters as InventoryPageParameters
from pages.parameters.cart_page_parameters import CartPageParameters
from tests.components.test_fill_checkout_from import fill_check_out_form_with_random_person_info_on_page
from tests.components.test_footer import check_footer_on_page
from tests.components.test_left_menu import check_left_menu_with_buttons_is_displayed_on_page

@allure.epic("SauceDemo Home Page")
@allure.feature("Default page state")
@allure.story("Default page state")
def test_main_page_default_state(main_page):
    main_page.open()
    main_page.main_page_logo_has_text(setting.LOGO)
    main_page.username_text_field_is_displayed()
    main_page.password_text_field_is_displayed()
    main_page.header_of_list_of_users_has_text(HomePageParameters.username_header)
    main_page.list_of_users_match_with(HomePageParameters.expected_list_of_logins)
    main_page.header_of_accepted_list_of_password_has_text(HomePageParameters.password_header)
    main_page.list_of_password_match_with(HomePageParameters.expected_passwords)
    main_page.error.empty_error_field_is_displayed()

@allure.epic("SauceDemo Inventory Page")
@allure.feature("Default page state")
@allure.story("Default page state")
def test_inventory_page_default_state_objects(inventory_page):
    inventory_page.page_components.page_logo_is_displayed_and_has_text(setting.LOGO)
    inventory_page.page_components.shopping_cart_icon_is_displayed()
    inventory_page.page_components.shopping_cart_image_is_on_page()
    inventory_page.check_static_image_request('GET', ImageName.shopping_card_image_name)
    inventory_page.check_static_image_request('GET', ImageName.cart_image_name)
    inventory_page.check_static_image_request('GET', ImageName.menu_image_name)
    inventory_page.check_static_image_request('GET', ImageName.arrow_image_name)
    inventory_page.check_static_image_request('GET', ImageName.filter_image_name)
    inventory_page.sort_is_displayed()
    inventory_page.page_components.check_header_of_page_title_has_text(InventoryPageParameters.header_of_product_title_text)
    inventory_page.products.description.check_product_by_index_is_in_json(0, setting.JSON_DIR)
    inventory_page.products.description.check_was_request_of_product_image_called_by_index(0)
    inventory_page.products.add_button.button_add_to_cart_by_index_is_displayed(0)
    inventory_page.sort_is_displayed()
    check_left_menu_with_buttons_is_displayed_on_page(inventory_page)
    check_footer_on_page(inventory_page)

@allure.epic("SauceDemo InventoryItem Page")
@allure.feature("Default page state")
@allure.story("Default page state")
def test_inventory_item_page_default_state(random_inventory_item_page, selected_random_product_name):
    check_left_menu_with_buttons_is_displayed_on_page(random_inventory_item_page)
    random_inventory_item_page.check_selected_product_from_inventory_page_is_right(selected_random_product_name)
    random_inventory_item_page.page_components.page_logo_is_displayed_and_has_text(setting.LOGO)
    random_inventory_item_page.page_components.shopping_cart_image_is_on_page()
    random_inventory_item_page.page_components.check_product_counter_icon_is_not_displayed()
    random_inventory_item_page.products.check_product_is_in_json(setting.JSON_DIR)
    random_inventory_item_page.products.button_add_to_cart_is_displayed()
    random_inventory_item_page.products.button_remove_to_cart_is_not_displayed()
    check_footer_on_page(random_inventory_item_page)

@allure.epic("SauceDemo Cart Page")
@allure.feature("Default page state")
@allure.story("Default page state")
def test_default_cart_page(inventory_page, cart_page):
    inventory_page.page_components.click_shopping_cart()
    check_left_menu_with_buttons_is_displayed_on_page(cart_page)
    cart_page.page_components.page_logo_is_displayed_and_has_text(setting.LOGO)
    cart_page.page_components.shopping_cart_icon_is_displayed()
    cart_page.page_components.check_product_counter_icon_is_not_displayed()
    cart_page.page_components.check_header_of_page_title_has_text(CartPageParameters.your_cart_label)
    cart_page.products.description.qty_label_has_text(CartPageParameters.qty_label)
    cart_page.products.description.description_label_has_text(CartPageParameters.description_label)
    cart_page.check_cart_list_is_empty()
    cart_page.continue_shopping_btn_has_text(CartPageParameters.continue_chopping_text)
    cart_page.checkout_btn_has_text(CartPageParameters.checkout_text)
    check_footer_on_page(cart_page)

@allure.epic("SauceDemo Checkout First Page")
@allure.feature("Default page state")
@allure.story("Default page state")
def test_check_out_first_page_default_state(inventory_page, cart_page, checkout_first_page):
    inventory_page.page_components.click_shopping_cart()
    cart_page.click_checkout_btn()
    check_left_menu_with_buttons_is_displayed_on_page(checkout_first_page)
    checkout_first_page.page_components.page_logo_is_displayed_and_has_text(setting.LOGO)
    checkout_first_page.page_components.check_header_of_page_title_has_text(CheckOutFirstPageParameters.page_title_text)
    checkout_first_page.page_components.shopping_cart_icon_is_displayed()
    checkout_first_page.page_components.check_product_counter_icon_is_not_displayed()
    checkout_first_page.check_first_name_field_is_displayed()
    checkout_first_page.check_last_name_field_is_displayed()
    checkout_first_page.check_postal_code_field_is_displayed()
    checkout_first_page.continue_btn_has_text(CheckOutFirstPageParameters.continue_btn_text)
    checkout_first_page.cancel_btn_has_text(CheckOutFirstPageParameters.cancel_btn)
    check_footer_on_page(checkout_first_page)

@allure.epic("SauceDemo Checkout Second Page")
@allure.feature("Default page state")
@allure.story("Default page state")
def test_check_out_second_page_default_state(inventory_page, cart_page, checkout_first_page, checkout_second_page):
    inventory_page.page_components.click_shopping_cart()
    cart_page.click_checkout_btn()
    fill_check_out_form_with_random_person_info_on_page(checkout_first_page)
    checkout_first_page.click_continue_btn()
    checkout_second_page.page_components.page_logo_is_displayed_and_has_text(setting.LOGO)
    checkout_second_page.page_components.shopping_cart_icon_is_displayed()
    checkout_second_page.page_components.check_product_counter_icon_is_not_displayed()
    checkout_second_page.page_components.check_header_of_page_title_has_text(CheckOutSecondPageParameters.overview_text)
    checkout_second_page.products.description.qty_label_has_text(CheckOutSecondPageParameters.qty_label)
    checkout_second_page.products.description.description_label_has_text(CheckOutSecondPageParameters.description_label)
    checkout_second_page.check_cart_list_is_empty()
    checkout_second_page.subtotal_price_label_has_text(CheckOutSecondPageParameters.item_total_text)
    checkout_second_page.tax_label_has_text(CheckOutSecondPageParameters.tax_text)
    checkout_second_page.total_price_has_text(CheckOutSecondPageParameters.total_text)
    checkout_second_page.cancel_btn_has_text(CheckOutSecondPageParameters.cancel_text)
    checkout_second_page.finish_btn_has_text(CheckOutSecondPageParameters.finish_text)
    check_left_menu_with_buttons_is_displayed_on_page(checkout_second_page)
    check_footer_on_page(checkout_second_page)

@allure.epic("SauceDemo Checkout Complete Page")
@allure.feature("Default page state")
@allure.story("Default page state")
def test_check_out_complete_page_default_state(inventory_page, cart_page, checkout_first_page, checkout_second_page,
                                               checkout_complete_page):
    inventory_page.page_components.click_shopping_cart()
    cart_page.click_checkout_btn()
    fill_check_out_form_with_random_person_info_on_page(checkout_first_page)
    checkout_first_page.click_continue_btn()
    checkout_second_page.click_finish_btn()
    checkout_complete_page.page_components.page_logo_is_displayed_and_has_text(setting.LOGO)
    checkout_complete_page.page_components.shopping_cart_icon_is_displayed()
    checkout_complete_page.page_components.check_product_counter_icon_is_not_displayed()
    checkout_complete_page.page_components.check_header_of_page_title_has_text(CheckOutCompletePageParameters.page_title_text)
    checkout_complete_page.complete_header_has_text(CheckOutCompletePageParameters.complete_header_text)
    checkout_complete_page.complete_text_has_text(CheckOutCompletePageParameters.complete_text)
    checkout_complete_page.back_home_btn_has_text(CheckOutCompletePageParameters.back_home_btn_text)