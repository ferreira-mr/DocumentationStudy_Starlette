from locale import locale_encoding_alias
from loguru import logger
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles

def homepage(request):
    logger.info(request.app.state.HELLO)
    logger.info(request.app)
    return PlainTextResponse('Hello, world!')

def user_me(request):
    username = "John Doe"
    return PlainTextResponse(f'Hello, {username}')

def user(request):
    username = request.path_params['username']
    return PlainTextResponse(f'Hello, {username}')

async def websocket_endpoint(websocket):
    await websocket.accept()
    await websocket.send_text('Hello, websocket')
    await websocket.close()

def startup():
    print('Ready to go')

routes = [
    Route('/', homepage),
    Route('/user/me', user_me),
    Route('/user/{username}', user),
    WebSocketRoute('/ws', websocket_endpoint),
    Mount('/static', StaticFiles(directory='static'))
]

app = Starlette(debug=True, routes=routes, on_startup=[startup])
app.state.HELLO = "Hello World!"
logger.info(app)