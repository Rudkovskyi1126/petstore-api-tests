import os
import uuid
import pytest
import requests
from dotenv import load_dotenv
load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    session.headers.update(
        {
        "Content-Type": "application/json",
        "Accept": "application/json",
        })
    yield session
    session.close()


@pytest.fixture
def user_payload():
    unique = uuid.uuid4().hex[:8]
    return {
        "id": 0,
        "username": f"test_user_{unique}",
        "firstName": "Test",
        "lastName": "User",
        "email": f"test_{unique}@example.com",
        "password": "password123",
        "phone": "1234567890",
        "userStatus": 1,
        }


@pytest.fixture
def created_user(api_client, base_url, user_payload):
    api_client.post(f"{base_url}/user", json=user_payload)
    yield user_payload
    api_client.delete(f"{base_url}/user/{user_payload['username']}")