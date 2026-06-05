from helpers.expect import expect


def test_create_and_get_pet(pet_helper, pet_payload):
    expect(pet_helper.create(pet_payload), code=200,
           reason="Creating a pet should return 200")

    response = pet_helper.get(pet_payload["id"])
    expect(response, code=200,
           reason="Fetching the created pet by ID should return 200")
    assert response.json()["name"] == pet_payload["name"], (
        "Pet name in response should match the name sent on creation"
    )

    pet_helper.delete(pet_payload["id"])


def test_delete_pet(pet_helper, pet_payload):
    pet_helper.create(pet_payload)

    expect(pet_helper.delete(pet_payload["id"]), code=200,
           reason="Deleting an existing pet should return 200")
    expect(pet_helper.get(pet_payload["id"]), code=404, message="Pet not found",
           reason="Fetching a deleted pet should return 404")


def test_update_pet(pet_helper, created_pet):
    updated = {**created_pet, "name": "Barsuk"}

    expect(pet_helper.update(updated), code=200,
           reason="Updating an existing pet should return 200")

    response = pet_helper.get(created_pet["id"])
    expect(response, code=200,
           reason="Fetching the updated pet should return 200")
    assert response.json()["name"] == "Barsuk", (
        "Pet name should reflect the value sent in the update request"
    )


def test_get_pets_by_status(pet_helper):
    response = pet_helper.find_by_status("available")
    expect(response, code=200,
           reason="Searching pets by status 'available' should return 200")
    assert len(response.json()) > 0, (
        "Response should contain at least one pet with status 'available'"
    )


def test_get_nonexistent_pet(pet_helper):
    expect(pet_helper.get(999_999_999), code=404, message="Pet not found",
           reason="Fetching a non-existent pet ID should return 404")


def test_create_pet_with_empty_name(pet_helper, pet_payload):
    pet_payload["name"] = ""
    expect(pet_helper.create(pet_payload), code=200,
           reason="Creating a pet with an empty name should still return 200")

    pet_helper.delete(pet_payload["id"])
