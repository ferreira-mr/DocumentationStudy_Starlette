from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
import uvicorn

routes = ...

middleware = [
    Middleware(TrustedHostMiddleware, allowed_hosts=['example.com', '*.example.com']),
    Middleware(HTTPSRedirectMiddleware)
]

app = Starlette(routes=routes, middleware=middleware)

uvicorn.run(app)