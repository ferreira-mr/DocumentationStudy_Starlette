from starlette.applications import Starlette
from starlette.routing import Route
from starlette.schemas import SchemaGenerator
import uvicorn


schemas = SchemaGenerator(
    {"openapi": "3.0.0", "info": {"title": "Example API", "version": "1.0"}}
)

def list_users(request):
    """
    responses:
      200:
        description: A list of users.
        examples:
          [{"username": "tom"}, {"username": "lucy"}]
    """
    raise NotImplementedError()


def create_user(request):
    """
    responses:
      200:
        description: A user.
        examples:
          {"username": "tom"}
    """
    raise NotImplementedError()


def openapi_schema(request):
    return schemas.OpenAPIResponse(request=request)


routes = [
    Route("/users", endpoint=list_users, methods=["GET"]),
    Route("/users", endpoint=create_user, methods=["POST"]),
    Route("/schema", endpoint=openapi_schema, include_in_schema=False)
]

app = Starlette(routes=routes)

uvicorn.run(app)
