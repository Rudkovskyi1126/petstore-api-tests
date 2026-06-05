# Petstore API Tests

[![API Tests](https://github.com/Rudkovskyi1126/petstore-api-tests/actions/workflows/ci.yml/badge.svg)](https://github.com/Rudkovskyi1126/petstore-api-tests/actions/workflows/ci.yml)

Automated API tests for the public [Petstore](https://petstore.swagger.io) API built with Python and pytest.

## Tech Stack

- Python 3.12
- pytest + pytest-html
- requests
- python-dotenv

## Project Structure

```
petstore-api-tests/
├── helpers/
│   ├── pet_helper.py      # PetHelper — wraps /pet endpoints
│   ├── store_helper.py    # StoreHelper — wraps /store endpoints
│   ├── user_helper.py     # UserHelper — wraps /user endpoints
│   └── expect.py          # expect(response, code, message) — assertion helper
├── tests/
│   ├── test_pet.py
│   ├── test_store.py
│   └── test_user.py
├── conftest.py            # fixtures: helpers, payloads, created_* resources
└── requirements.txt
```

## Test Coverage

**Pet** (`tests/test_pet.py`)
- Create a pet and get it by ID
- Delete a pet
- Update a pet
- Find pets by status
- Get a non-existent pet (404)
- Create a pet with an empty name

**Store** (`tests/test_store.py`)
- Create an order
- Get an order by ID
- Delete an order
- Get inventory

**User** (`tests/test_user.py`)
- Create a user
- Get a user by username
- Update a user
- Delete a user

## How To Run

Create a `.env` file in the project root:

```
BASE_URL=https://petstore.swagger.io/v2
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest -v
```

Generate an HTML report:

```bash
pytest -v --html=report/index.html --self-contained-html
```

## CI/CD

Tests run automatically via GitHub Actions on every push and pull request to `main`.

After each push to `main` a test report is published to GitHub Pages:
**https://rudkovskyi1126.github.io/petstore-api-tests/**
