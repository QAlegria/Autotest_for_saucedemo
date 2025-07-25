
def test_product_sort(inventory_page):
    inventory_page.check_products_is_a_to_z_sorted()
    inventory_page.click_sort()
    inventory_page.select_z_to_a_sort()
    inventory_page.check_products_is_z_to_a_sorted()
    inventory_page.click_sort()
    inventory_page.select_low_to_high_sort()
    inventory_page.check_low_to_high_products_sort()
    inventory_page.click_sort()
    inventory_page.select_high_to_low_sort()
    inventory_page.check_high_to_low_products_sort()
    inventory_page.select_a_to_z_sort()
    inventory_page.check_products_is_a_to_z_sorted()


def test_first_product_add_to_cart_and_remove(inventory_page):
    inventory_page.page_components.check_product_counter_icon_is_not_displayed()
    inventory_page.products.add_button.button_add_to_cart_by_index_is_displayed(0)
    inventory_page.products.add_button.click_button_add_to_card_product_by_index(0)
    inventory_page.page_components.check_product_counter_icon_is(1)
    inventory_page.products.remove_button.click_button_remove_from_cart_product_by_index(0)
    inventory_page.page_components.check_product_counter_icon_is_not_displayed()


def test_add_and_remove_random_products(inventory_page, prod_list):
    inventory_page.page_components.check_product_counter_icon_is_not_displayed()
    inventory_page.add_random_products_to_cart(prod_list)
    inventory_page.check_product_counter_icon_is_equals_random_selected_products()
    inventory_page.remove_random_products_from_cart(prod_list)
    inventory_page.check_product_counter_icon_is_equals_selected_minus_removed_products()



