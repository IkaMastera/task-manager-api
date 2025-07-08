def test_root_route(base_url, session):
    response = session.get(f"{base_url}/")
    assert response.status_code == 200