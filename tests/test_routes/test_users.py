import json


def test_create_user(client):
    data = {"username": "string",
            "email": "user@example.com",
            "password": "123456"}
    response = client.post("/users", json.dumps(data))
    assert response.status_code == 200
