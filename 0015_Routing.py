from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route
import uvicorn



async def homepage(request):
    return PlainTextResponse("Homepage")

async def about(reques):
    return PlainTextResponse("About")

routes = [
    Route("/", endpoint=homepage),
    Route("/about", endpoint=about)
]

app = Starlette(routes=routes)

uvicorn.run(app)
