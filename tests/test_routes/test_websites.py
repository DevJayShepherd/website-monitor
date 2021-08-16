import json


def test_add_website(client):
    data = {
        "website_name": "string",
        "website_url": "string",
        "website_description": "string",
        "website_keywords": "string"
    }

    response = client.post("/website/add_website", json.dumps(data))
    assert response.status_code == 200


def test_retrieve_website_by_id(client):
    data = {
        "website_name": "string",
        "website_url": "string",
        "website_description": "string",
        "website_keywords": "string"
    }
    client.post("/website/add_website", json.dumps(data))
    response = client.get("/website/get/1")
    assert response.status_code == 200



