import pytest

def test_root_route(base_url, session):
    response = session.get(f"{base_url}/")
    assert response.status_code == 200

#Basic Availability Test
def test_get_all_tasks(base_url, session):
    response = session.get(f"{base_url}/tasks ")
    assert response.status_code == 200

# Create Valid Task
def test_create_task(base_url, session):
    payload = {"title": "Write docs", "completed": False}
    response = session.post(f"{base_url}/tasks", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()

# Create a test for invalid payload
def test_create_task_invalid_payload(base_url, session):
    payload = {"Invalid_field": "Oops"}
    response = session.post(f"{base_url}/tasks", json=payload)
    assert response.status_code == 400

# Create a test task for user updating information
def test_update_tasl(base_url, session):
    payload = {"title": "Temp task", "completed": False}
    response = session.post(f"{base_url}/tasks", json=payload)
    task_id = response.json().get("id")

    update = {"title": "Updated task", "completed": True}
    response = session.put(f"{base_url}/tasks/{task_id}", json=update)
    assert response.status_code in [200, 204]

# Read specific task test
def test_get_task_by_id(base_url, session):
    payload = {"title": "Fetch me", "completed": False}
    response = session.post(f"{base_url}/tasks", json=payload)
    task_id = response.json()["id"]

    res = session.get(f"{base_url}/tasks/{task_id}")
    assert response.status_code == 200
    assert res.json()["title"] == "Fetch me"

# Delete test for task
def test_delete_task(base_url, session):
    payload = {"title": "Delete me", "completed": False}
    response = session.post(f"{base_url}/tasks", json=payload)
    task_id = response.json()["id"]

    response = session.delete(f"{base_url}/tasks/{task_id}")
    assert response.status_code in [200, 204]

    response = session.get(f"{base_url}/tasks/{task_id}")
    assert response.status_code == 404

# Not Found Check
def test_get_invalid_task(base_url, session):
    response = session.get(f"{base_url}/tasks/9sadasdasa99")
    assert response.status_code == 404






@pytest.mark.parametrize("endpoint, expected", [
    ("/tasks", 200),
    ("/nonexistent", 404),
])
def test_multiple_endpoints(base_url, session, endpoint, expected):
    response = session.get(f"{base_url}{endpoint}")
    assert response.status_code == expected