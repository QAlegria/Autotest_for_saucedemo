
class ProductComponentLocators:
    product_item = '[data-test="inventory-item"]'

    product_name_header = '[data-test="inventory-item-name"]'
    product_description = '[data-test="inventory-item-desc"]'
    product_price = '[data-test="inventory-item-price"]'
    button_to_remove_from_cart = '.btn_secondary[id*="remove"]'

    nearest_item = 'xpath=ancestor::div[contains(@data-test,"inventory-item")]'
