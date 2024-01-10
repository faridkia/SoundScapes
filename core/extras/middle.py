# Middleware.py | stack
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.middleware_stack = []

    def __call__(self, request):
        # Request phase
        for middleware in self.middleware_stack:
            request = middleware.process_request(request)

        # Execute the view
        response = self.get_response(request)

        # Response phase
        for middleware in reversed(self.middleware_stack):
            response = middleware.process_response(request, response)

        return response

    def add_middleware(self, middleware):
        self.middleware_stack.append(middleware)

# # settings.py
# MIDDLEWARE = [
#     # Other middleware components...
#     'yourapp.middleware.SimpleMiddleware',
# ]