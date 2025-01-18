import sys
sys.path.append('C:/Users/SUNIL SONI/Desktop/Mahesh/API_Testing_Using_Python')
from utils.api_client import APIClient

client = APIClient()

def test_get_posts():
    response = client.get("/posts")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert len(response.json()) > 0, "No posts found"

def test_get_single_post():
    response = client.get("/posts/1")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    print(data)
    assert "id" in data, "'id' not found in the response"
    assert data["id"] == 1, f"Expected ID 1, got {data['id']}"

def test_create_post():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = client.post("/posts", payload=payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    data = response.json()
    assert "id" in data, "'id' not found in the response"
    assert data["title"] == "foo", f"Expected title 'foo', got {data['title']}"

def test_update_post():
    payload = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }
    response = client.put("/posts/1", payload=payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert data["title"] == "Updated Title", f"Expected 'Updated Title', got {data['title']}"

def test_delete_post():
    response = client.delete("/posts/1")
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
