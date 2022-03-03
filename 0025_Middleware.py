from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware import Middleware
from starlette.applications import Starlette

class CustomHeaderMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, header_value='Example'):
        super().__init__(app)
        self.header_value = header_value

    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers['Custom'] = self.header_value
        return response

routes = ...

middleware = [
    Middleware(CustomHeaderMiddleware, header_value='Customized')
]

app = Starlette(routes=routes, middleware=middleware)
