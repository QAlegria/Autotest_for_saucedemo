from time import sleep

from config import setting
from pages.parameters.inventory_page_parameters import InventoryPageParameters as Parameters
from tests.components.test_footer import check_footer_on_page
from tests.components.test_left_menu import check_left_menu_with_buttons_is_displayed_on


def test_log_out(inventory_page):
    inventory_page.left_menu.click_left_menu_button()
    inventory_page.left_menu.click_logout_button()
    inventory_page.check_url_is(setting.HOME_PAGE_URL)


def test_inventory_page_default_state_objects(inventory_page):
    inventory_page.inventory_page_logo_is_displayed_and_has_text(Parameters.inventory_page_header)
    inventory_page.shopping_cart_image_is_displayed()
    inventory_page.shopping_cart_image_is_on_page()
    inventory_page.check_static_image_request('GET', Parameters.shopping_card_image_name)
    inventory_page.check_static_image_request('GET', Parameters.cart_image_name)
    inventory_page.check_static_image_request('GET', Parameters.menu_image_name)
    inventory_page.check_static_image_request('GET', Parameters.arrow_image_name)
    inventory_page.check_static_image_request('GET', Parameters.filter_image_name)
    inventory_page.sort_is_displayed()
    inventory_page.header_of_product_title_has_text(Parameters.header_of_product_title_text)
    inventory_page.check_product_by_index_is_in_json(0, setting.JSON_DIR)
    inventory_page.check_was_request_of_product_image_called_by_index(0)
    inventory_page.button_add_to_cart_by_index_is_displayed(0)
    inventory_page.sort_is_displayed()
    check_left_menu_with_buttons_is_displayed_on(inventory_page)
    check_footer_on_page(inventory_page)

def test_product_sort(inventory_page):
    inventory_page.check_products_is_a_to_z_sorted()
    inventory_page.click_sort()
    inventory_page.select_z_to_a_sort()
    inventory_page.check_products_is_z_to_a_sorted()
    inventory_page.click_sort()
    inventory_page.select_low_to_high_sort()
    inventory_page.check_low_to_high_products_sort()
    inventory_page.click_sort()
    inventory_page.select_high_to_low_sort()
    inventory_page.check_high_to_low_products_sort()
    inventory_page.select_a_to_z_sort()
    inventory_page.check_products_is_a_to_z_sorted()


def test_first_product_add_to_cart_and_remove(inventory_page):
    inventory_page.check_product_counter_icon_is_not_displayed()
    inventory_page.button_add_to_cart_by_index_is_displayed(0)
    inventory_page.click_button_add_to_card_product_by_index(0)
    inventory_page.check_product_counter_icon_is(1)
    inventory_page.click_button_remove_from_cart_product_by_index(0)
    inventory_page.check_product_counter_icon_is_not_displayed()


def test_add_and_remove_random_products(inventory_page, prod_list):
    inventory_page.check_product_counter_icon_is_not_displayed()
    inventory_page.add_random_products_to_cart(prod_list)
    inventory_page.check_product_counter_icon_is_equals_random_selected_products()
    inventory_page.remove_random_products_from_cart(prod_list)
    inventory_page.check_product_counter_icon_is_equals_selected_minus_removed_products()


def test_moving_to_cart_page(inventory_page):
    inventory_page.click_shopping_cart()
    inventory_page.check_url_is(setting.CART_PAGE_URL)

