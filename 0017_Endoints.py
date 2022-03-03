from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.endpoints import HTTPEndpoint
from starlette.routing import Route
import uvicorn


class Homepage(HTTPEndpoint):
    async def get(self, request):
        return PlainTextResponse(f"Hello, world!")


class User(HTTPEndpoint):
    async def get(self, request):
        username = request.path_params["username"]
        return PlainTextResponse(f"Hello, {username}")


routes = [
    Route("/", Homepage),
    Route("/{username}", User)
]

app = Starlette(routes=routes)

uvicorn.run(app)