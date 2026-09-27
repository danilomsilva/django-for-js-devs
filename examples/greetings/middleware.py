import time


class TimingMiddleware:
    """Adds an X-Response-Time-Ms header. A minimal, concrete example of the
    request/response pipeline described in docs/04-request-lifecycle.md.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.monotonic()
        response = self.get_response(request)
        elapsed_ms = (time.monotonic() - start) * 1000
        response["X-Response-Time-Ms"] = f"{elapsed_ms:.2f}"
        return response
