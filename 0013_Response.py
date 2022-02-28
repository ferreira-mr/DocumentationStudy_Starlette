from starlette.responses import FileResponse
import uvicorn


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    response = FileResponse('static/hello.txt')
    await response(scope, receive, send)


uvicorn.run(app)