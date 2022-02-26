from urllib import response
from starlette.responses import PlainTextResponse
import uvicorn


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Hello, world!')
    await response(scope, receive,send)

uvicorn.run(app)