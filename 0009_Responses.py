from unittest import async_case
from urllib import response
from starlette.responses import JSONResponse
import uvicorn


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = JSONResponse({'hello': 'world'})
    await response(scope, receive, send)

uvicorn.run(app)