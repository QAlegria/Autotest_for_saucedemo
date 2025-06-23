from pages.parameters.inventory_page_parameters import InventoryPageParameters


def test_inventory_page_objects(checking_inventory_page, get_image_api):
    checking_inventory_page.checking_the_inventory_page_logo()
    checking_inventory_page.checking_shopping_cart_image()
    # Should I insert parameters, or is there another way to do it?
    get_image_api.get_image_request(InventoryPageParameters.shopping_card_image_name)
    get_image_api.checking_response_body()
    checking_inventory_page.checking_left_slide_button()
    checking_inventory_page.checking_filter_is_exist()
    checking_inventory_page.checking_header_of_product_title()
    checking_inventory_page.click_left_slide_button()
    checking_inventory_page.checking_left_menu()
    checking_inventory_page.click_close_button()
    checking_inventory_page.checking_first_product_card_name_and_description()
    checking_inventory_page.checking_first_product_card_image()
