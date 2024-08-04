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

def test_read_todo():
    # First, create a todo
    create_response = client.post("/todos/", json={"title": "Read Todo", "description": "Todo to be read", "completed": False})
    todo_id = create_response.json()["id"]

    # Now, read the todo
    read_response = client.get(f"/todos/{todo_id}")
    assert read_response.status_code == 200
    assert read_response.json()["title"] == "Read Todo"
    assert read_response.json()["description"] == "Todo to be read"
    assert read_response.json()["completed"] == False
    assert read_response.json()["id"] == todo_id

def test_update_todo():
    # First, create a todo
    create_response = client.post("/todos/", json={"title": "Update Todo", "description": "Todo to be updated", "completed": False})
    todo_id = create_response.json()["id"]

    # Now, update the todo
    update_response = client.put(f"/todos/{todo_id}", json={"title": "Updated Todo", "description": "Todo has been updated", "completed": True})
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "Updated Todo"
    assert update_response.json()["description"] == "Todo has been updated"
    assert update_response.json()["completed"] == True
    assert update_response.json()["id"] == todo_id

def test_delete_todo():
    # First, create a todo
    create_response = client.post("/todos/", json={"title": "Delete Todo", "description": "Todo to be deleted", "completed": False})
    todo_id = create_response.json()["id"]

    # Now, delete the todo
    delete_response = client.delete(f"/todos/{todo_id}")
    assert delete_response.status_code == 204

    # Verify that the todo is deleted
    read_response = client.get(f"/todos/{todo_id}")
    assert read_response.status_code == 404