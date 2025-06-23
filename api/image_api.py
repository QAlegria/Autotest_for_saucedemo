import requests
from config import setting

class ImageApi:
    def __init__(self):
        self.image_url = setting.STATIC_IMAGE_URL
        self.response_body_text = None


    def get_image_request(self, image_name):
        response = requests.get(
            f'{self.image_url}{image_name}',
            headers={'Content-type': 'image/svg+xml'}
        )
        response.raise_for_status()
        self.response_body_text = response.text
        return response

    def checking_response_body(self):
        assert self.response_body_text.startswith('<svg')
        assert self.response_body_text.endswith('</svg>')
