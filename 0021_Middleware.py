from starlette.applications import Starlette
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware import Middleware

routes = ...

middleware = [
    Middleware(HTTPSRedirectMiddleware)
]

app = Starlette(routes=routes, middleware=middleware)