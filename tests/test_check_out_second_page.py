from config import setting
from pages.parameters.check_out_second_page_parameters import CheckOutSecondPageParameters
from tests.components.test_footer import check_footer_on_page
from tests.components.test_left_menu import check_left_menu_with_buttons_is_displayed_on

def test_check_out_second_page_default_state(check_out_second_page):
    check_left_menu_with_buttons_is_displayed_on(check_out_second_page)
    check_out_second_page.page_components.shopping_cart_icon_is_displayed()
    check_out_second_page.page_components.check_product_counter_icon_is_not_displayed()
    check_out_second_page.page_components.check_header_of_product_title_has_text(CheckOutSecondPageParameters.overview_text)
    check_out_second_page.products.description.qty_label_has_text(CheckOutSecondPageParameters.qty_label)
    check_out_second_page.products.description.description_label_has_text(CheckOutSecondPageParameters.description_label)
    check_out_second_page.check_cart_list_is_empty()
    check_out_second_page.subtotal_price_label_has_text('Item total: ')
    check_out_second_page.tax_label_has_text(r'Tax: \$')
    check_out_second_page.total_price_has_text(r'Total: \$')
    check_out_second_page.cancel_btn_has_text(CheckOutSecondPageParameters.cancel_text)
    check_out_second_page.finish_btn_has_text(CheckOutSecondPageParameters.finish_text)
    check_footer_on_page(check_out_second_page)

def test_integration(inventory_page, page_switcher, prod_list):
    inventory_page.page_components.check_product_counter_icon_is_not_displayed()
    inventory_page.add_random_products_to_cart(prod_list)
    inventory_page.check_product_counter_icon_is_equals_random_selected_products()
    cart_page = page_switcher.switch_to_cart_page()
    cart_page.page_components.check_product_counter_icon_is(len(prod_list))
    cart_page.products.description.check_all_product_is_in_json(setting.JSON_DIR)
    cart_page.check_prod_list_from_inventory_page_is_right(prod_list)
    check_out_first_page = page_switcher.switch_to_check_out_first_page()
    check_out_second_page = page_switcher.switch_to_check_out_second_page()
    check_out_second_page.check_subtotal_price_is_summing_right()
    check_out_second_page.check_tax_is_counting_right()
    check_out_second_page.check_total_price_is_counting_right()
    check_out_complete_page = page_switcher.switch_to_check_out_complete_page()
    check_out_complete_page.complete_header_has_text('Thank you for your order!')
    check_out_complete_page.complete_text_has_text('Your order has been dispatched, and will arrive just as fast as the pony can get there!')