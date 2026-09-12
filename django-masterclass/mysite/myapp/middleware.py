class LogRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Before view
        print(f"[Middleware] Request path: {request.path}")
        # Let request continue
        response = self.get_response(request)

        # After view
        print(f"[Middleware] Response Status: {response.status_code}")
        # Let response continue
        return response
