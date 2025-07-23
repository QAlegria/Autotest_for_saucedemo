# from pages.check_out_fisrt_page import CheckOutFirstPage
from pages.checkout_complete_page import CheckOutCompletePage
from pages.checkout_first_page import CheckOutFirstPage
from pages.checkout_second_page import CheckOutSecondPage
from pages.inventory_item_page import InventoryItemPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.locators.components.cart_and_page_components import PageComponentsLocators
from pages.locators.components.navigation_component_locators import NavigationComponentLocators



from config import setting
from tests.components.test_fill_checkout_from import fill_check_out_form_with_random_person_info


class PageSwitcher:
    def __init__(self, page):
        self.page = page

    def switch_to_inventory_page(self) -> InventoryPage:
        self.page.click(NavigationComponentLocators.back_btn)
        self.page.wait_for_url(f"**{setting.INVENTORY_PAGE_URL}")
        self.page.wait_for_load_state("load")
        return InventoryPage(self.page)

    def switch_to_cart_page(self) -> CartPage:
        self.page.click(PageComponentsLocators.shopping_cart)
        self.page.wait_for_url(f"**{setting.CART_PAGE_URL}")
        self.page.wait_for_load_state("load")
        return CartPage(self.page)

    def switch_to_inventory_item_page(self, locator) -> InventoryItemPage:
        locator.click()
        self.page.wait_for_url(f"**{setting.INVENTORY_ITEM_PAGE_URL}")
        self.page.wait_for_load_state("load")
        return InventoryItemPage(self.page)

    def switch_to_check_out_first_page(self) -> CheckOutFirstPage:
        self.page.click(NavigationComponentLocators.continue_btn)
        self.page.wait_for_url(f"**{setting.CHECK_OUT_FIRST_PAGE_URL}")
        self.page.wait_for_load_state("load")
        return CheckOutFirstPage(self.page)

    def switch_to_check_out_second_page(self) -> CheckOutSecondPage:
        fill_check_out_form_with_random_person_info(CheckOutFirstPage(self.page))
        self.page.click(NavigationComponentLocators.continue_btn)
        self.page.wait_for_url(f"**{setting.CHECK_OUT_SECOND_PAGE_URL}")
        self.page.wait_for_load_state("load")
        return CheckOutSecondPage(self.page)

    def switch_to_check_out_complete_page(self) -> CheckOutCompletePage:
        self.page.click(NavigationComponentLocators.continue_btn)
        self.page.wait_for_url(f"**{setting.CHECK_OUT_COMPLETE_PAGE_URL}")
        self.page.wait_for_load_state("load")
        return CheckOutCompletePage(self.page)