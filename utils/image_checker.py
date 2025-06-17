from config import setting
class ImageChecker:
    @staticmethod
    def checking_image_link_of_element(element, image_name):
        image_style = element.evaluate("element => getComputedStyle(element).backgroundImage")
        expected_image_link = f'{setting.STATIC_IMAGE_URL}{image_name}'
        assert expected_image_link in image_style