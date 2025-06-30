

from playwright.sync_api import Page, Request, Response

IMAGE_BY_MIME: dict[str, bytes] = {
    "image/svg+xml": b"<svg",
    "image/jpeg":    b"\xFF\xD8",
    "image/png":     b"\x89PNG\r\n\x1A\n",
}

class NetworkWatcher:
    def __init__(self, page: Page):
        self.page = page
        self.captured_requests: list[Request] = []
        self.captured_responses: list[Response] = []

    def _on_request(self, req: Request):
        self.captured_requests.append(req)

    def _on_response(self, res: Response):
        self.captured_responses.append(res)

    def start_tracking(self):
        self.page.on('request', self._on_request)
        self.page.on('response', self._on_response)

    def end_tracking(self):
        self.page.remove_listener('request', self._on_request)
        self.page.remove_listener('response', self._on_response)

    def was_url_requested(self, method: str = 'GET', url: str = None):
        return any(url in req.url and req.method == method for req in self.captured_requests)

    def was_url_response_ok(self, url):
        return any(url in res.url and res.status == 200 for res in self.captured_responses)

    def was_url_double_requested(self, url):
        count = 0
        req_set = set()
        for req in self.captured_requests:
            if url in req.url:
                key = (req.method, req.url, req.post_data or '')
                if key in req_set:
                    count += 1
                else:
                    req_set.add(key)
        return count

    def request_by_url_method(self, method, url) -> Request:
        return next(req for req in self.captured_requests if url in req.url and req.method == method)

    def response_by_url_method(self, method, url) -> Response:
        return next(res for res in self.captured_responses if self.request_by_url_method(url, method) == res.request and res.status == 200)

    def check_image_response_body_by_method_url(self, method, url):
        image_response = self.response_by_url_method(url, method)
        assert image_response, f"No response found for {method} {url}"

        mime = image_response.headers.get("content-type","").split(";")[0]
        expected_image = IMAGE_BY_MIME.get(mime)
        assert expected_image, f"Unhandled MIME type: {mime}"

        body = image_response.body()
        assert body.startswith(expected_image), (f"Body of {url!r} doesn't match expected signature for {mime}"
    )
