import pytest
from utils.logger import get_logger

logger = get_logger()

def test_root_route(base_url, session):
    logger.info("Testing root route...")
    try:
        response = session.get(f"{base_url}/")
        logger.info(f"Status Code: {response.status_code}")
        assert response.status_code == 200
    except Exception as e:
        logger.error(f"test_root_route failed: {str(e)}")
        raise
    
#Basic Availability Test
def test_get_all_tasks(base_url, session):
    logger.info("Testing get all tasks...")
    try:
        response = session.get(f"{base_url}/posts")
        logger.info(f"Status Code: {response.status_code}")
        assert response.status_code == 200
    except Exception as e:
        logger.error(f"test_get_all_tasks failed: {str(e)}")
        raise

# Create Valid Task
def test_create_task(base_url, session):
    logger.info("Testing create task...")
    try:
        payload = {"title": "Write docs", "completed": False}
        response = session.post(f"{base_url}/posts", json=payload)
        assert response.status_code == 201
        assert "id" in response.json()
    except Exception as e:
        logger.error(f"test_create_task failed: {str(e)}")
        raise

# Create a test for invalid payload
def test_create_task_invalid_payload(base_url, session):
    logger.info("Testing create task with invalid payload...")
    try:
        payload = {"Invalid_field": "Oops"}
        response = session.post(f"{base_url}/comments", json=payload)
        assert response.status_code in [201, 200]
    except Exception as e:
        logger.error(f"test_create_task_invalid_payload failed: {str(e)}")
        raise

# Get all comments for a post
def test_get_all_comments_for_post(base_url, session):
    logger.info("Testing get all comments for a post...")
    try:
        post_id = 1
        response = session.get(f"{base_url}/posts/{post_id}/comments")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert all("email" in comment for comment in data)
    except Exception as e:
        logger.error(f"test_get_all_comments_for_post failed: {str(e)}")
        raise

# Delete test for task

def test_delete_task(base_url, session):
    logger.info("Testing delete task...")
    try:
        payload = {"title": "Delete me", "completed": False}
        response = session.post(f"{base_url}/posts", json=payload)
        task_id = response.json()["id"]

        response = session.delete(f"{base_url}/posts/{task_id}")
        assert response.status_code in [200, 204]

        response = session.get(f"{base_url}/posts/{task_id}")
        assert response.status_code == 404
    except Exception as e:
        logger.error(f"test_delete_task failed: {str(e)}")
        raise

# Not Found Check
def test_get_invalid_task(base_url, session):
    logger.info("Testing get invalid task...")
    try:
        response = session.get(f"{base_url}/posts/999999")
        assert response.status_code == 404
    except Exception as e:
        logger.error(f"test_get_invalid_task failed: {str(e)}")
        raise

# Response time under threshold
def test_response_time_under_500ms(base_url, session):
    logger.info("Testing response time under 500ms...")
    try:
        response = session.get(f"{base_url}/posts")
        assert response.elapsed.total_seconds() < 0.5
    except Exception as e:
        logger.error(f"test_response_time_under_500ms failed: {str(e)}")
        raise


@pytest.mark.parametrize("endpoint, expected", [
    ("/posts", 200),
    ("/nonexistent", 404),
])

def test_multiple_endpoints(base_url, session, endpoint, expected):
    logger.info(f"Testing endpoint: {endpoint} with expected status code: {expected}")
    try:
        response = session.get(f"{base_url}{endpoint}")
        logger.info(f"Status Code: {response.status_code}")
        assert response.status_code == expected
    except Exception as e:
        logger.error(f"test_multiple_endpoints failed for {endpoint}: {str(e)}")
        raise