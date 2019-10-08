from webob import Request, Response


class API:
    def __init__(self):
        """ Defined a dict called self.routes where we will be storing
            paths as keys and handlers as values.
        """
        self.routes = {}

    def route(self, path):
        """ Take path as an argument and in the wrapper method simply
            put this path in the self.routes dictionary as a key and
            the handler as a value.
        """
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper

    def __call__(self, environ, start_response):

        request = Request(environ)

        response = self.handle_request(request)

        return response(environ, start_response)

    def handle_request(self, request):
        """ When a request comes in, we need to check its path,
            find an appropriate handler, call that handler &
            return an appropriate response.
        """

        response = Response()

        handler = self.find_handler(request_path=request.path)

        if handler is not None:
            handler(request, response)
        else:
            self.default_response(response)
        return response

    def default_response(self, response):
        response.status_code = 404
        response.text = "Not found"

    def find_handler(self, request_path):
        for path, handler in self.routes.items():
            if path == request_path:
                return handler
