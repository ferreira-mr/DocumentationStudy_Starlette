from urllib import response
from starlette.responses import PlainTextResponse, RedirectResponse
import uvicorn


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    if scope['path'] != '/':
        response = RedirectResponse(url='/')
    else:
        response = PlainTextResponse('Hello, world!')
    await response(scope, receive, send)


uvicorn.run(app)
