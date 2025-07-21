import random
from typing import Callable, TypeVar
from decimal import Decimal, ROUND_HALF_UP

T = TypeVar("T")

class PriceHelper:
    @staticmethod
    def get_price_and_currency_from_text(text: str, current_currency: str) -> str:
        price_tuple = text.partition(current_currency)
        return price_tuple[1]+price_tuple[2]

    @staticmethod
    def get_product_price(price_from_page: str):
        if price_from_page[0].isdigit():
            return price_from_page
        return price_from_page[1:]

    @staticmethod
    def get_product_price_currency(price_from_page: str):
        if price_from_page[0].isdigit():
            raise ValueError("Expected not digit value")
        return price_from_page[:1]

    @staticmethod
    def get_decimal_price(prices_from_page: str):
        return Decimal(prices_from_page).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    @staticmethod
    def get_decimal_prices(prices_from_page: list[str]):
        return [Decimal(PriceHelper.get_product_price(price)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
                for price in prices_from_page]

    @staticmethod
    def sum_product_prices(list_of_prices):
        return sum(list_of_prices)

    @staticmethod
    def get_decimal_price_from_text(text: str,  current_currency: str):
        price_and_currency = PriceHelper.get_price_and_currency_from_text(text, current_currency)
        price_str = PriceHelper.get_product_price(price_and_currency)
        return PriceHelper.get_decimal_price(price_str)

    @staticmethod
    def tax_price(tax_percent: int, price) -> Decimal:
        return Decimal(tax_percent * price/100).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


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
    def low_to_high_sort(numbers: list[Decimal]) -> bool:
        return numbers == sorted(numbers)

    @staticmethod
    def high_to_low_sort(numbers: list[Decimal]) -> bool:
        return numbers == sorted(numbers, reverse=True)

class RandomItems:

    @staticmethod
    def get_random_count(count):
        return random.randint(1, count)

    @staticmethod
    def select_one_random_item(count, action: Callable[[int], T]) ->T:
        print(f'{count} is count of btn')
        if count == 0:
            raise ValueError("No items left to select")
        uniq_indexes = random.sample(range(count), 1)
        print(f'{uniq_indexes[0]+1} is chosen item')
        return action(uniq_indexes[0])

    @staticmethod
    def repeat_random_amount_once_each(times, action: Callable[[], None]):
        print(f'times of iteration {times}')
        if times == 0:
            raise ValueError("No items left to select")
        for i in range(times):
            action()
