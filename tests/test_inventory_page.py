from time import sleep

from config import setting
from pages.parameters.inventory_page_parameters import InventoryPageParameters as Parameters


def test_inventory_page_objects(inventory_page_with_standard_user, get_image_api):
    inventory_page_with_standard_user.inventory_page_logo_is_displayed_and_has_text(Parameters.inventory_page_header)
    inventory_page_with_standard_user.shopping_cart_image_is_displayed()
    inventory_page_with_standard_user.shopping_cart_image_is_on_page()
    get_image_api.get_image_request_with_image_name(Parameters.shopping_card_image_name)
    get_image_api.checking_svg_response_body()
    inventory_page_with_standard_user.left_menu_button_is_displayed()
    inventory_page_with_standard_user.filter_is_displayed()
    inventory_page_with_standard_user.header_of_product_title_has_text(Parameters.header_of_product_title_text)
    inventory_page_with_standard_user.click_left_menu_button()
    inventory_page_with_standard_user.button_to_main_menu_is_displayed()
    inventory_page_with_standard_user.button_about_is_displayed()
    inventory_page_with_standard_user.logout_button_is_displayed()
    inventory_page_with_standard_user.reset_button_is_displayed()
    inventory_page_with_standard_user.click_close_button()
    inventory_page_with_standard_user.check_product_by_index_is_in_json(0, setting.JSON_DIR)
