from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles
import uvicorn


routes = [
    Mount('/static', app=StaticFiles(directory='static'), name='static')
]

app = Starlette(routes=routes)


uvicorn.run(app)