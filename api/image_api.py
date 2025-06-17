import requests

class ImageApi:
    def __init__(self):
        self.url = 'https://www.saucedemo.com/static/media/'
        self.response_body_text = None


    def get_image(self, image_url):
        response = requests.get(
            f'{self.url}{image_url}',
            headers={'Content-type': 'image/svg+xml'}
        )
        response.raise_for_status()
        self.response_body_text = response.text()
        print(self.response_body_text)
        return response
