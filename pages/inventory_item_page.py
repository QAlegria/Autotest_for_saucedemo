from pages.base_page import BasePage
from pages.components.cart_and_page_component import PageComponents
from pages.components.footer_component import FooterComponents
from pages.components.left_menu_component import LeftMenu
from pages.components.product_component import InventoryProducts, InventoryItem


class InventoryItemPage(BasePage):
    # Working with logo, cart_icon, title
    @property
    def page_components(self):
        return PageComponents(self.page)

    # Working with left menu
    @property
    def left_menu(self):
        return LeftMenu(self.page)

    # Working with product cards
    @property
    def products(self):
        return InventoryItem(self.page, self.network)

    def check_selected_product_from_inventory_page_is_right(self, product_name):
        assert self.products.get_product_name() == product_name

    # Social media and terms elements
    @property
    def footer(self):
        return FooterComponents(self.page)