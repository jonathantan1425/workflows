from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestUser:
    def test_get_users(self):
        resp = client.get("/users")
        assert resp.status_code == 200
        assert resp.json() == {"msg": "Hello World"}
