# Petstore API Tests

Automated API tests for the public [Petstore](https://petstore.swagger.io) API built with Python and pytest.

## Tech Stack
- Python 3.x
- pytest
- requests
- Allure Reports

## Test Coverage
- Create a pet (POST)
- Get a pet by ID (GET)
- Update a pet (PUT)
- Delete a pet (DELETE)
- Find pets by status (GET)

## How To Run

Install dependencies:

pip install -r requirements.txt

Run tests:

pytest


## CI/CD
Tests run automatically via GitHub Actions on every push.