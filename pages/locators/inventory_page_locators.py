from pages.locators.components.common_components import CommonComponents


class InventoryPageLocators:
    inventory_page_logo = CommonComponents.inventory_page_logo

    shopping_cart = CommonComponents.shopping_cart
    shopping_cart_counter = CommonComponents.shopping_cart_counter

    product_sort = '.product_sort_container'
    az_sort_selector = 'az'
    za_sort_selector = 'za'
    low_to_high_sort_selector = 'lohi'
    high_to_low_sort_selector = 'hilo'

    header_of_product_title = CommonComponents.title

    list_of_products = '.inventory_list'
    nearest_product_card = 'xpath=ancestor::div[contains(@class,"inventory_item")]'
    product_container = '.inventory_item'
    product_image = '.inventory_item_img img'
    product_name_header = CommonComponents.product_name_header
    product_description = CommonComponents.product_description
    product_price = CommonComponents.product_price
    button_add_to_cart = '.btn_primary'
    button_to_remove_from_cart = CommonComponents.button_to_remove_from_cart

