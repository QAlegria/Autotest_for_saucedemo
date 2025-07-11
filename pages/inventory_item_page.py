from pages.base_page import BasePage
from pages.components.cart_and_page_components import PageComponents
from pages.components.footer_components import FooterComponents
from pages.components.left_menu_component import LeftMenu
from pages.components.product_components import InventoryProducts


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
        return InventoryItemPage(self.page, self.network)

    # Social media and terms elements
    @property
    def footer(self):
        return FooterComponents(self.page)