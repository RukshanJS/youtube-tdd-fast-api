from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_todo():
    response = client.post("/todos/", json={"title": "Test Todo", "description": "Test Description", "completed": False})
    print(response.content)  # Keep this for debugging if needed
    assert response.status_code == 201
    assert response.json()["title"] == "Test Todo"
    assert response.json()["description"] == "Test Description"
    assert response.json()["completed"] == False
    assert "id" in response.json()

