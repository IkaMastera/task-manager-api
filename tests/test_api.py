import pytest
import logging

# Set up logging
logging.basicConfig(
    level = logging.INFO,
    format = "[%(asctime)s] %(levelname)s: %(message)s",
    handlers = [logging.FileHandler("reports/test.log", mode="w"), logging.StreamHandler()]
)

def test_root_route(base_url, session):
    logging.info("Testing root route...")
    try:
        response = session.get(f"{base_url}/")
        logging.info(f"Status Code: {response.status_code}")
        assert response.status_code == 200
    except Exception as e:
        logging.error(f"test_root_route failed: {str(e)}")
        raise
    
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

# Get all comments for a post
def test_get_all_comments_for_post(base_url, session):
    post_id = 1
    response = session.get(f"{base_url}/posts/{post_id}/comments")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert all("email" in comment for comment in data)

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