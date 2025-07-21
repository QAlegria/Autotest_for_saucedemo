
class ProductComponentLocators:
    product_item = '[data-test="inventory-item"]'

    product_name_header = '[data-test="inventory-item-name"]'
    product_description = '[data-test="inventory-item-desc"]'
    product_price = '[data-test="inventory-item-price"]'
    button_to_remove_from_cart = '.btn_secondary[id*="remove"]'
    product_image = 'img[data-test*="item"][data-test$="img"]'

    nearest_item = 'xpath=ancestor::div[contains(@data-test,"inventory-item")]'

    qty_label = '.cart_quantity_label'
    description_label = '.cart_desc_label'

    cart_quantity = '.cart_quantity'