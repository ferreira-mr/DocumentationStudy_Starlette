import uvicorn
from starlette.applications import Starlette
from starlette.routing import WebSocketRoute


async def websocket_index(websocket):
    await websocket.accept()
    await websocket.send_text("Hello, websocket!")
    await websocket.close()


async def websocket_user(websocket):
    name = websocket.path_params["name"]
    await websocket.accept()
    await websocket.send_text(f"Hello, {name}")
    await websocket.close()


routes = [
    WebSocketRoute("/", endpoint=websocket_index),
    WebSocketRoute("/{name}", endpoint=websocket_user),
]


app = Starlette(routes=routes)


uvicorn.run(app)
