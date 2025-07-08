from time import sleep

from config import setting
from tests.components.test_footer import check_footer_on_page
from tests.components.test_left_menu import check_left_menu_with_buttons_is_displayed_on


def test_default_cart_page(cart_page):
    check_left_menu_with_buttons_is_displayed_on(cart_page)
    sleep(3)
    check_footer_on_page(cart_page)


def test_integration_with_inventory_and_cart_page_add_and_remove_items(inventory_page, page_switcher, prod_list):
    inventory_page.check_product_counter_icon_is_not_displayed()
    inventory_page.add_random_products_to_cart(prod_list)
    inventory_page.check_product_counter_icon_is_equals_random_selected_products()
    inventory_page.remove_random_products_from_cart(prod_list)
    inventory_page.check_product_counter_icon_is_equals_selected_minus_removed_products()
    cart_page = page_switcher.switch_to_cart_page()
    cart_page.check_all_product_is_in_json(setting.JSON_DIR)
    cart_page.check_prod_list_from_inventory_page_is_right(prod_list)
