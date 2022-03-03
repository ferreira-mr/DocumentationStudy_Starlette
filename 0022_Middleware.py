from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.trustedhost import TrustedHostMiddleware

routes = ...

middleware = [
    Middleware(TrustedHostMiddleware, allowed_hosts=['example.com', '*.example.com'])
]

app = Starlette(routes=routes, middleware=middleware)