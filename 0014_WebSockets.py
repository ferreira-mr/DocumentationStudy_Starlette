from starlette.websockets import WebSocket
import uvicorn


async def app(scope, receive, send):
    assert scope['type'] == 'websocket', 'Websocket connection is required'
    websocket = WebSocket(scope=scope, receive=receive, send=send)
    await websocket.accept()
    await websocket.send_text('Hello, World!')
    await websocket.close()

uvicorn.run(app)