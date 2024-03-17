from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_add_task():
    response = client.post("/add/", params={"new_task": "Task 1"})
    assert response.status_code == 200
    assert response.json() == "Task 1"


def test_read_list():
    response = client.get("/list/")
    assert response.status_code == 200
    assert response.json() == {"1": "Task 1"}


def test_complete_task():
    response = client.post("/complete/", params={"task_id": 1})
    assert response.status_code == 200
    assert response.json() == "Task 1 deleted successfully!"


def test_delete_list():
    response = client.get("/delete/")
    assert response.status_code == 200
    assert response.json() == {}


def test_complete_nonexistent_task():
    response = client.post("/complete/", params={"task_id": 100})
    assert response.status_code == 404
    assert response.json() == {'detail': 'Task not found'}
