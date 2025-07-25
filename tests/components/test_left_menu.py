
def check_left_menu_with_buttons_is_displayed_on_page(page_with_left_menu):
    page_with_left_menu.left_menu.left_menu_button_is_displayed()
    page_with_left_menu.left_menu.click_left_menu_button()
    page_with_left_menu.left_menu.button_to_main_menu_is_displayed()
    page_with_left_menu.left_menu.button_about_is_displayed()
    page_with_left_menu.left_menu.logout_button_is_displayed()
    page_with_left_menu.left_menu.reset_button_is_displayed()
    page_with_left_menu.left_menu.click_close_button()
