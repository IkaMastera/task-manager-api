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





@pytest.mark.parametrize("endpoint, expected", [
    ("/tasks", 200),
    ("/nonexistent", 404),
])
def test_multiple_endpoints(base_url, session, endpoint, expected):
    response = session.get(f"{base_url}{endpoint}")
    assert response.status_code == expected