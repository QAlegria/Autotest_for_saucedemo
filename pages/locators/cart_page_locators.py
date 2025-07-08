from pages.locators.components.common_components import CommonComponents


class CartPageLocators:
    cart_page_logo = CommonComponents.inventory_page_logo

    shopping_cart = CommonComponents.shopping_cart
    shopping_cart_counter = CommonComponents.shopping_cart_counter

    your_cart_title = CommonComponents.title

    qty_label = '.cart_quantity_label'
    description_label = '.cart_desc_label'

    btn_continue_shop = '.btn#continue-shopping'
    btn_checkout = '.btn#checkout'

    list_of_cart_products = '.cart_list'
    cart_product_container = '.cart_item'
    product_name_header = CommonComponents.product_name_header
    product_description = CommonComponents.product_description
    product_price = CommonComponents.product_price
    button_to_remove_from_cart = CommonComponents.button_to_remove_from_cart
    cart_quantity = '.cart_quantity'
    nearest_product_card = '.cart_item_label'

