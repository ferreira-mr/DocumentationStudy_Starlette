from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware import Middleware
from starlette.applications import Starlette

class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers['Custom'] = 'Example'
        return response

middleware = [
    Middleware(CustomHeaderMiddleware)
]

routes = ...

app = Starlette(routes=routes, middleware=middleware)