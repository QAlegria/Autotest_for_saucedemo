from config import setting
from pages.parameters.checkout_complete_page import CheckOutCompletePageParameters
from tests.components.test_fill_checkout_from import fill_check_out_form_with_random_person_info_on_page

def test_log_out(inventory_page):
    inventory_page.left_menu.click_left_menu_button()
    inventory_page.left_menu.click_logout_button()
    inventory_page.check_url_is(setting.HOME_PAGE_URL)

def test_moving_to_random_product_item_page(inventory_page):
    inventory_page.click_on_random_product_on_page()
    inventory_page.check_url_is(setting.INVENTORY_ITEM_PAGE_URL)

def test_moving_to_cart_page(inventory_page):
    inventory_page.page_components.click_shopping_cart()
    inventory_page.check_url_is(setting.CART_PAGE_URL)

def test_inventory_item_page_integration_add_button_one_product(random_inventory_item_page, cart_page,
                                                                selected_random_product_name, prod_list):
    random_inventory_item_page.check_selected_product_from_inventory_page_is_right(selected_random_product_name)
    random_inventory_item_page.page_components.check_product_counter_icon_is_not_displayed()
    random_inventory_item_page.products.click_add_to_cart(prod_list)
    random_inventory_item_page.page_components.check_product_counter_icon_is(1)
    random_inventory_item_page.page_components.click_shopping_cart()
    random_inventory_item_page.check_url_is(setting.CART_PAGE_URL)
    cart_page.page_components.check_product_counter_icon_is(1)
    cart_page.products.description.check_all_product_is_in_json(setting.JSON_DIR)
    cart_page.check_prod_list_from_inventory_page_is_right(prod_list)

def test_integration_with_inventory_and_cart_page_add_and_remove_items(inventory_page, cart_page, prod_list):
    inventory_page.page_components.check_product_counter_icon_is_not_displayed()
    inventory_page.add_random_products_to_cart(prod_list)
    inventory_page.check_product_counter_icon_is_equals_random_selected_products()
    inventory_page.remove_random_products_from_cart(prod_list)
    inventory_page.check_product_counter_icon_is_equals_selected_minus_removed_products()
    inventory_page.page_components.click_shopping_cart()
    inventory_page.check_url_is(setting.CART_PAGE_URL)
    cart_page.page_components.check_product_counter_icon_is(len(prod_list))
    cart_page.products.description.check_all_product_is_in_json(setting.JSON_DIR)
    cart_page.check_prod_list_from_inventory_page_is_right(prod_list)

def test_e2e_process_with_random_products(inventory_page, cart_page, checkout_first_page, checkout_second_page,
                                          checkout_complete_page, prod_list):
    inventory_page.page_components.check_product_counter_icon_is_not_displayed()
    inventory_page.add_random_products_to_cart(prod_list)
    inventory_page.check_product_counter_icon_is_equals_random_selected_products()
    inventory_page.page_components.click_shopping_cart()
    inventory_page.check_url_is(setting.CART_PAGE_URL)
    cart_page.page_components.check_product_counter_icon_is(len(prod_list))
    cart_page.products.description.check_all_product_is_in_json(setting.JSON_DIR)
    cart_page.check_prod_list_from_inventory_page_is_right(prod_list)
    cart_page.click_checkout_btn()
    cart_page.check_url_is(setting.CHECK_OUT_FIRST_PAGE_URL)
    fill_check_out_form_with_random_person_info_on_page(checkout_first_page)
    checkout_first_page.click_continue_btn()
    checkout_first_page.check_url_is(setting.CHECK_OUT_SECOND_PAGE_URL)
    checkout_second_page.check_subtotal_price_is_summing_right()
    checkout_second_page.check_tax_is_counting_right()
    checkout_second_page.check_total_price_is_counting_right()
    checkout_second_page.click_finish_btn()
    checkout_second_page.check_url_is(setting.CHECK_OUT_COMPLETE_PAGE_URL)
    checkout_complete_page.complete_text_has_text(CheckOutCompletePageParameters.complete_text)
    checkout_complete_page.back_home_btn_has_text(CheckOutCompletePageParameters.back_home_btn_text)