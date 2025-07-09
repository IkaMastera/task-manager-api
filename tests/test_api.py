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




@pytest.mark.parametrize("endpoint, expected", [
    ("/tasks", 200),
    ("/nonexistent", 404),
])
def test_multiple_endpoints(base_url, session, endpoint, expected):
    response = session.get(f"{base_url}{endpoint}")
    assert response.status_code == expected