from time import sleep

from config import setting
from pages.parameters.inventory_page_parameters import InventoryPageParameters as Parameters


def test_inventory_page_default_state_objects(inventory_page_with_standard_user):
    inventory_page_with_standard_user.inventory_page_logo_is_displayed_and_has_text(Parameters.inventory_page_header)
    inventory_page_with_standard_user.shopping_cart_image_is_displayed()
    inventory_page_with_standard_user.shopping_cart_image_is_on_page()
    inventory_page_with_standard_user.check_static_image_request('GET',Parameters.shopping_card_image_name)
    inventory_page_with_standard_user.check_static_image_request('GET',Parameters.cart_image_name)
    inventory_page_with_standard_user.check_static_image_request('GET',Parameters.menu_image_name)
    inventory_page_with_standard_user.check_static_image_request('GET',Parameters.arrow_image_name)
    inventory_page_with_standard_user.check_static_image_request('GET',Parameters.filter_image_name)
    inventory_page_with_standard_user.left_menu_button_is_displayed()
    inventory_page_with_standard_user.sort_is_displayed()
    inventory_page_with_standard_user.header_of_product_title_has_text(Parameters.header_of_product_title_text)
    inventory_page_with_standard_user.click_left_menu_button()
    inventory_page_with_standard_user.button_to_main_menu_is_displayed()
    inventory_page_with_standard_user.button_about_is_displayed()
    inventory_page_with_standard_user.logout_button_is_displayed()
    inventory_page_with_standard_user.reset_button_is_displayed()
    inventory_page_with_standard_user.click_close_button()
    inventory_page_with_standard_user.check_product_by_index_is_in_json(0, setting.JSON_DIR)
    inventory_page_with_standard_user.check_was_request_of_product_image_called_by_index(0)
    inventory_page_with_standard_user.add_to_cart_by_index_is_displayed(0)
    inventory_page_with_standard_user.sort_is_displayed()
    inventory_page_with_standard_user.twitter_is_displayed()
    inventory_page_with_standard_user.facebook_is_displayed()
    inventory_page_with_standard_user.linkedin_is_displayed()
    inventory_page_with_standard_user.terms_footer_is_displayed()
    inventory_page_with_standard_user.click_and_check_twitter_is_opened()
    inventory_page_with_standard_user.click_and_check_facebook_is_opened()
    inventory_page_with_standard_user.click_and_check_linkedin_is_opened()

def test_product_sort(inventory_page_with_standard_user):
    inventory_page_with_standard_user.check_products_is_a_to_z_sorted()
    inventory_page_with_standard_user.click_sort()
    inventory_page_with_standard_user.select_z_to_a_sort()
    inventory_page_with_standard_user.check_products_is_z_to_a_sorted()
    inventory_page_with_standard_user.click_sort()
    inventory_page_with_standard_user.select_low_to_high_sort()
    inventory_page_with_standard_user.check_low_to_high_products_sort()
    inventory_page_with_standard_user.click_sort()
    inventory_page_with_standard_user.select_high_to_low_sort()
    inventory_page_with_standard_user.check_high_to_low_products_sort()