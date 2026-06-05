import os
import random
import uuid
import pytest
import requests
from dotenv import load_dotenv

from helpers.pet_helper import PetHelper
from helpers.store_helper import StoreHelper
from helpers.user_helper import UserHelper

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json",
    })
    yield session
    session.close()


# --- Helpers ---

@pytest.fixture(scope="session")
def pet_helper(api_client, base_url):
    return PetHelper(api_client, base_url)


@pytest.fixture(scope="session")
def store_helper(api_client, base_url):
    return StoreHelper(api_client, base_url)


@pytest.fixture(scope="session")
def user_helper(api_client, base_url):
    return UserHelper(api_client, base_url)


# --- Pet fixtures ---

@pytest.fixture
def pet_payload():
    unique_id = random.randint(100_000, 999_999)
    return {
        "id": unique_id,
        "name": f"pet_{unique_id}",
        "status": "available",
        "photoUrls": ["https://example.com/pet.jpg"],
    }


@pytest.fixture
def created_pet(pet_helper, pet_payload):
    pet_helper.create(pet_payload)
    yield pet_payload
    pet_helper.delete(pet_payload["id"])


# --- Store fixtures ---

@pytest.fixture
def order_payload(created_pet):
    return {
        "id": random.randint(100_000, 999_999),
        "petId": created_pet["id"],
        "quantity": 1,
        "shipDate": "2026-05-17T11:36:00.229Z",
        "status": "placed",
        "complete": True,
    }


@pytest.fixture
def created_order(store_helper, order_payload):
    store_helper.create_order(order_payload)
    yield order_payload
    store_helper.delete_order(order_payload["id"])


# --- User fixtures ---

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
def created_user(user_helper, user_payload):
    user_helper.create(user_payload)
    yield user_payload
    user_helper.delete(user_payload["username"])
