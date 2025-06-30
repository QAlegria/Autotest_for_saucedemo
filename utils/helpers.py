from playwright.sync_api import Locator


class PriceHelper:
    @staticmethod
    def get_price(price_from_page: str):
        if price_from_page[0].isdigit():
            return price_from_page
        return price_from_page[1:]

    @staticmethod
    def get_currency(price_from_page: str):
        if price_from_page[0].isdigit():
            raise ValueError("Expected not digit value")
        return price_from_page[:1]

    @staticmethod
    def get_float_prices(prices_from_page: list[str]):
        return [float(PriceHelper.get_price(price)) for price in prices_from_page]


class LoginDivideHelper:
    @staticmethod
    def text_to_divide_from_page(element):
        text_from_element = element.inner_text()
        list_of_text = [line.strip() for line in text_from_element.splitlines() if line.strip()]
        list_of_logins = list_of_text[1:]
        return list_of_logins

class ProductSort:
    @staticmethod
    def a_to_z_sort(strings: list[str]):
        return strings == sorted(strings, key=lambda s: s.lower())

    @staticmethod
    def z_to_a_sort(strings: list[str]) -> bool:
        return strings == sorted(strings, key=lambda s: s.lower(), reverse=True)

    @staticmethod
    def low_to_high_sort(numbers: list[float]) -> bool:
        return numbers == sorted(numbers)

    @staticmethod
    def high_to_low_sort(numbers: list[float]) -> bool:
        return numbers == sorted(numbers, reverse=True)