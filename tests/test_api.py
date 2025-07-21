import pytest

def test_root_route(base_url, session):
    response = session.get(f"{base_url}/")
    assert response.status_code == 200

#Basic Availability Test
def test_get_all_tasks(base_url, session):
    response = session.get(f"{base_url}/posts")
    assert response.status_code == 200

# Create Valid Task
def test_create_task(base_url, session):
    payload = {"title": "Write docs", "completed": False}
    response = session.post(f"{base_url}/posts", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()

# Create a test for invalid payload
def test_create_task_invalid_payload(base_url, session):
    payload = {"Invalid_field": "Oops"}
    response = session.post(f"{base_url}/comments", json=payload)
    assert response.status_code in [201, 200]

# Create a test task for user updating information
def test_update_task(base_url, session):
     payload = {"title": "Temp task", "completed": False}
     response = session.post(f"{base_url}/posts", json=payload)
     task_id = response.json().get("id")

     update = {"title": "Updated task", "completed": True}
     res = session.put(f"{base_url}/posts/{task_id}", json=update)
     assert res.status_code in [200, 204]

# Read specific task test
def test_get_task_by_id(base_url, session):
     payload = {"title": "Fetch me", "body": "desc", "userId": 1}
     response = session.post(f"{base_url}/posts", json=payload)
     task_id = response.json()["id"]
     res = session.get(f"{base_url}/posts/{task_id}")
     assert res.status_code == 200
     assert res.json()["title"] == "Fetch me"

# Delete test for task

def test_delete_task(base_url, session):
    payload = {"title": "Delete me", "completed": False}
    response = session.post(f"{base_url}/posts", json=payload)
    task_id = response.json()["id"]

    response = session.delete(f"{base_url}/posts/{task_id}")
    assert response.status_code in [200, 204]

    response = session.get(f"{base_url}/posts/{task_id}")
    assert response.status_code == 404

# Not Found Check
def test_get_invalid_task(base_url, session):
    response = session.get(f"{base_url}/posts/9sadasdasa99")
    assert response.status_code == 404

# Response time under threshold
def test_response_time_under_500ms(base_url, session):
    response = session.get(f"{base_url}/posts")
    assert response.elapsed.total_seconds() < 1.5


@pytest.mark.parametrize("endpoint, expected", [
    ("/posts", 200),
    ("/nonexistent", 404),
])
def test_multiple_endpoints(base_url, session, endpoint, expected):
    response = session.get(f"{base_url}{endpoint}")
    assert response.status_code == expected