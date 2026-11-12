import os
from fastapi.testclient import TestClient

os.environ["DATABASE_URL"] = "postgresql://localhost/test"
from app.main import app


def test_health():
    response = TestClient(app).get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
