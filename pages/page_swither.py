from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.locators.inventory_page_locators import InventoryPageLocators as Inv_locators
from pages.locators.cart_page_locators import CartPageLocators as Cart_Locators
from config import setting

class PageSwitcher:
    def __init__(self, page):
        self.page = page

    def switch_to_cart_page(self) -> CartPage:
        self.page.click(Inv_locators.shopping_cart)
        self.page.wait_for_url(f"**{setting.CART_PAGE_URL}")
        self.page.wait_for_load_state("load")
        return CartPage(self.page)

    def switch_to_inventory_page(self) -> InventoryPage:
        self.page.click(Cart_Locators.btn_continue_shop)
        self.page.wait_for_url(f"**{setting.INVENTORY_PAGE_URL}")
        self.page.wait_for_load_state("load")
        return InventoryPage(self.page)
