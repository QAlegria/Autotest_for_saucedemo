import json


class JsonWorker:
    data = None

    def open_file(self, json_file):
        with open(json_file, encoding='utf-8') as jw:
            self.data = json.load(jw)


    def get_product_by_conditions(self, **conditions):
        return [
            product for product in self.data
            if all(product.get(key) == value for key, value in conditions.items())
        ]

