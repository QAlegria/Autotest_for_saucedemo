# from pages.check_out_fisrt_page import CheckOutFirstPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.locators.components.cart_and_page_components import PageComponentsLocators
from pages.locators.cart_page_locators import CartPageLocators as Cart_Locators

from config import setting

class PageSwitcher:
    def __init__(self, page):
        self.page = page

    def switch_to_cart_page(self) -> CartPage:
        self.page.click(PageComponentsLocators.shopping_cart)
        self.page.wait_for_url(f"**{setting.CART_PAGE_URL}")
        self.page.wait_for_load_state("load")
        return CartPage(self.page)

    def switch_to_inventory_page(self) -> InventoryPage:
        self.page.click(Cart_Locators.btn_continue_shop)
        self.page.wait_for_url(f"**{setting.INVENTORY_PAGE_URL}")
        self.page.wait_for_load_state("load")
        return InventoryPage(self.page)

    # def switch_to_check_out_first_page(self) -> CheckOutFirstPage:
    #     self.page.click(Cart_Locators.btn_checkout)
    #     self.page.wait_for_url(f"**{setting.CHECK_OUT_FIRST_PAGE_URL}")
    #     self.page.wait_for_load_state("load")
    #     return CheckOutFirstPage(self.page)