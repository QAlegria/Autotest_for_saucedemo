from pages.parameters.inventory_page_parameters import InventoryPageParameters


def test_inventory_page_objects(inventory_page_standard_user, get_image_api):
    inventory_page_standard_user.checking_the_inventory_page_logo()
    inventory_page_standard_user.checking_shopping_cart_image()
    # Should I insert parameters, or is there another way to do it?
    get_image_api.get_image_request(InventoryPageParameters.shopping_card_image_name)
    get_image_api.checking_response_body()
    inventory_page_standard_user.checking_left_slide_button()
    inventory_page_standard_user.checking_filter_is_exist()
    inventory_page_standard_user.checking_header_of_product_title()
    inventory_page_standard_user.click_left_slide_button()
    inventory_page_standard_user.checking_left_menu()
    inventory_page_standard_user.click_close_button()
    # Made one test checking_first_product instead 3 alternative
    # checking_inventory_page.checking_first_product_card_name_and_description()
    # checking_inventory_page.checking_first_product_card_image()
    # checking_inventory_page.checking_first_product_card_price()
    inventory_page_standard_user.checking_first_product()