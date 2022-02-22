from starlette.responses import PlainTextResponse

async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Hello, world!')
    await response(scope, receive, send)

# gunicorn -w 4 -k uvicorn.workers.UvicornWorker --log-level warning example:app
# gunicorn -k uvicorn.workers.UvicornH11Worker 0002_Introduction:app