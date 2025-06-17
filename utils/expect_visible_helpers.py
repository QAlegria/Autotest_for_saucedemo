from playwright.sync_api import expect


class ExpectVisibleElements:
    @staticmethod
    def expect_visible_elements(elements):
        total_of_elements = elements.count()
        for element in range(total_of_elements):
            expect(elements.nth(element)).to_be_visible()