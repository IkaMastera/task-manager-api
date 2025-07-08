import pytest

def test_root_route(base_url, session):
    response = session.get(f"{base_url}/")
    assert response.status_code == 200


@pytest.mark.parametrize("endpoint, expected", [
    ("/tasks", 200),
    ("/nonexistent", 404),
])
def test_multiple_endpoints(base_url, session, endpoint, expected):
    response = session.get(f"{base_url}{endpoint}")
    assert response.status_code == expected