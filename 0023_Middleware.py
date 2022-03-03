from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.gzip import GZipMiddleware


routes = ...

middleware = [
    Middleware(GZipMiddleware, minimum_size=1000)
]


app = Starlette(routes=routes, middleware=middleware)