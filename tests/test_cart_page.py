from time import sleep

from config import setting
from pages.parameters.cart_page_parameters import CartPageParameters
from tests.components.test_footer import check_footer_on_page
from tests.components.test_left_menu import check_left_menu_with_buttons_is_displayed_on


def test_default_cart_page(cart_page):
    check_left_menu_with_buttons_is_displayed_on(cart_page)
    cart_page.page_components.shopping_cart_icon_is_displayed()
    cart_page.page_components.check_product_counter_icon_is_not_displayed()
    cart_page.page_components.header_of_product_title_has_text(CartPageParameters.your_cart_label)
    cart_page.products.qty_label_has_text(CartPageParameters.qty_label)
    cart_page.products.description_label_has_text(CartPageParameters.description_label)
    cart_page.check_cart_list_is_empty()
    cart_page.continue_shopping_btn_has_text(CartPageParameters.continue_chopping_text)
    cart_page.checkout_btn_has_text(CartPageParameters.checkout_text)
    check_footer_on_page(cart_page)


# make part of inv test funct test like it did with components test?
def test_integration_with_inventory_and_cart_page_add_and_remove_items(inventory_page, page_switcher, prod_list):
    inventory_page.page_components.check_product_counter_icon_is_not_displayed()
    inventory_page.add_random_products_to_cart(prod_list)
    inventory_page.check_product_counter_icon_is_equals_random_selected_products()
    inventory_page.remove_random_products_from_cart(prod_list)
    inventory_page.check_product_counter_icon_is_equals_selected_minus_removed_products()
    cart_page = page_switcher.switch_to_cart_page()
    cart_page.page_components.check_product_counter_icon_is(len(prod_list))
    cart_page.products.check_all_product_is_in_json(setting.JSON_DIR)
    cart_page.products.check_prod_list_from_inventory_page_is_right(prod_list)
