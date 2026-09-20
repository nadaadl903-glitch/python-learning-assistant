from fastapi.testclient import TestClient
from app.main import app


def test_successful_request():
    with TestClient(app) as client:
        response = client.post(
            "/query",
            json={"question": "What is a Python exception?"}
        )

        assert response.status_code == 200

        data = response.json()

        assert "answer" in data
        assert "sources" in data


def test_invalid_input():
    with TestClient(app) as client:
        response = client.post(
            "/query",
            json={}
        )

        assert response.status_code == 422