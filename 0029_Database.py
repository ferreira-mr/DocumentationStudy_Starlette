import databases
import sqlalchemy
from starlette.applications import Starlette
from starlette.config import Config
from starlette.responses import JSONResponse
from starlette.routing import Route
import uvicorn

config = Config('.env')
DATABASE_URL = config('DATABASE_URL')

metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)

database = databases.Database(DATABASE_URL)


async def list_notes(request):
    query = notes.select()
    result = await database.fetch_all(query)
    content = [{
        "text": result["text"],
        "completed": result["completed"]
    } for result in result]
    return JSONResponse(content)


async def add_note(request):
    data = await request.json()
    query = notes.insert().values(text=data["text"],
                                  completed=data["completed"])
    await database.execute(query)
    return JSONResponse({"text": data["text"], "completed": data["completed"]})


# Database transactions are available either as a decorator, as a context manager, or a low-level API.


# Using a decorator on an endpoint:
@databases.transaction()
async def populate_note(request):
    # This database insert occurs within a transaction.
    # It will be rolled back by the `RuntimeError`
    query = notes.insert().values(text="you won't see me", completed=True)
    await database.execute(query)
    raise RuntimeError()


# Using a context manager:
async def populate_note(request):
    async with database.transaction():
        # This database insert occurs within a transaction.
        # It will be rolled back by the `RuntimeError`.
        query = notes.insert().values(text="you won't see me", completed=True)
        await request.database.execute(query)
        raise RuntimeError()


# Using the low-level API
async def populate_a_note(request):
    transaction = await database.transaction()
    try:
        # This database insert occurs within a transaction.
        # It will be rolled back by the RuntimeError
        query = notes.insert().values(text="you wont't see me", completed=True)
        await database.execute(query)
        raise RuntimeError()
    except:
        await transaction.rollback()
        raise
    else:
        await transaction.commit()


routes = [
    Route("/notes", endpoint=list_notes, methods=["GET"]),
    Route("/notes", endpoint=add_note, methods=["POST"]),
]

app = Starlette(routes=routes,
                on_startup=[database.connect],
                on_shutdown=[database.disconnect])

uvicorn.run(app)