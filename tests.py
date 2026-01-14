from fastapi.testclient import TestClient
from app.main import app
import pytest
from app.storage import clear_tasks

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_storage():
    clear_tasks()


def test_get_tasks_initially_empty():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []


def test_create_task():
    response = client.post("/tasks", json={"title": "Test task"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test task"
    assert data["completed"] is False
    assert "id" in data


def test_get_tasks_after_creation():
    client.post("/tasks", json={"title": "Task 1"})
    response = client.get("/tasks")
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Task 1"


def test_update_task():
    client.post("/tasks", json={"title": "Old"})
    response = client.put("/tasks/1", json={"title": "New", "completed": True})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New"
    assert data["completed"] is True


def test_update_nonexistent_task():
    response = client.put("/tasks/999", json={"title": "X"})
    assert response.status_code == 404


def test_delete_task():
    client.post("/tasks", json={"title": "To delete"})
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


def test_get_tasks_after_deletion():
    client.post("/tasks", json={"title": "Temp"})
    client.delete("/tasks/1")
    response = client.get("/tasks")
    assert response.json() == []
