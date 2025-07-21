from config import setting
from tests.components.test_footer import check_footer_on_page
from tests.components.test_left_menu import check_left_menu_with_buttons_is_displayed_on


def test_inventory_item_page_default_state(random_inventory_item_page, selected_random_product_name):
    check_left_menu_with_buttons_is_displayed_on(random_inventory_item_page)
    random_inventory_item_page.check_selected_product_from_inventory_page_is_right(selected_random_product_name)
    random_inventory_item_page.page_components.page_logo_is_displayed_and_has_text(setting.LOGO)
    random_inventory_item_page.page_components.shopping_cart_image_is_on_page()
    random_inventory_item_page.page_components.check_product_counter_icon_is_not_displayed()
    random_inventory_item_page.products.check_product_is_in_json(setting.JSON_DIR)
    random_inventory_item_page.products.button_add_to_cart_is_displayed()
    random_inventory_item_page.products.button_remove_to_cart_is_not_displayed()
    check_footer_on_page(random_inventory_item_page)

def test_inventory_item_page_integration_add_button_one_product(random_inventory_item_page, page_switcher, selected_random_product_name, prod_list):
    random_inventory_item_page.check_selected_product_from_inventory_page_is_right(selected_random_product_name)
    random_inventory_item_page.page_components.check_product_counter_icon_is_not_displayed()
    random_inventory_item_page.products.click_add_to_cart(prod_list)
    random_inventory_item_page.page_components.check_product_counter_icon_is(1)
    cart_page = page_switcher.switch_to_cart_page()
    cart_page.page_components.check_product_counter_icon_is(1)
    cart_page.products.description.check_all_product_is_in_json(setting.JSON_DIR)
    cart_page.check_prod_list_from_inventory_page_is_right(prod_list)
