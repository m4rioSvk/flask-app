import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_returns_message(client):
    response = client.get("/")
    data = response.get_json()
    assert "message" in data
    assert data["status"] == "ok"


def test_about_status_code(client):
    response = client.get("/about")
    assert response.status_code == 200


def test_about_returns_author(client):
    response = client.get("/about")
    data = response.get_json()
    assert data["author"] == "Mario"


def test_unknown_route_returns_404(client):
    response = client.get("/somethingfake")
    assert response.status_code == 404
