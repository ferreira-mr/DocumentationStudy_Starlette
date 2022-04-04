from starlette.responses import HTMLResponse
from starlette.testclient import TestClient

from chapter_0029_Database import app


def test_list_notes():
    client = TestClient(app)
    response = client.get('/notes')
    assert response.status_code == 200