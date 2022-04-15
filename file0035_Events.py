from starlette.applications import Starlette


async def some_startup_task():
    pass

async def some_shutdown_task():
    pass

routes = [
    ...
]

app = Starlette(
    routes=routes,
    on_startup=[some_startup_task],
    on_shutdown=[some_shutdown_task]
)
