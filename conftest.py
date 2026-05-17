import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def base_url():
    return os.getenv("BASE_URL")