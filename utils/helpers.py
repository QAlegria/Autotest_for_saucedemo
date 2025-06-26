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

class LoginDivideHelper:
    @staticmethod
    def text_to_divide_from_page(element):
        text_from_element = element.inner_text()
        list_of_text = [line.strip() for line in text_from_element.splitlines() if line.strip()]
        list_of_logins = list_of_text[1:]
        return list_of_logins