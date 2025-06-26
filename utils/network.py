from playwright.sync_api import Page, Request, Response

class NetworkWatcher:
    def __init__(self, page: Page):
        self.page = page
        self.captured_requests: list[Request] = []
        self.captured_responses: list[Response] = []

    def _on_request(self, req: Request):
        self.captured_requests.append(req)

    def _on_response(self, res: Response):
        self.captured_responses.append(res)

    # def __enter__(self):
    #     self.page.on('request', self._on_request)
    #     self.page.on('response', self._on_response)
    #
    # def __exit__(self):
    #     self.page.remove_listener('request', self._on_request)
    #     self.page.remove_listener('response', self._on_response)

    def start_tracking(self):
        self.page.on('request', self._on_request)
        self.page.on('response', self._on_response)

    def end_tracking(self):
        self.page.remove_listener('request', self._on_request)
        self.page.remove_listener('response', self._on_response)

    def was_url_requested(self, url):
        return any(url in req.url for req in self.captured_requests)

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