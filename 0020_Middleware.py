from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware


routes = ...

middleware = [
    Middleware(CORSMiddleware, allow_origins=['8'])
]

app = Starlette(routes=routes, middleware=middleware)