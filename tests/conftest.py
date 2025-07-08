import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:8000"

@pytest.fixture(scope="function")
def session():
    return requests.Session()