from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user():
    response = client.post("/users/register", json={
        "name": "John Doe",
        "email": "johndoe@example.com",
        "password": "securepass"
    })
    assert response.status_code == 200

def test_invalid_email():
    response = client.post("/users/register", json={
        "name": "Jane",
        "email": "invalidemail",
        "password": "pass"
    })
    assert response.status_code == 422