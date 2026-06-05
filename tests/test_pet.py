def test_create_and_get_pet(pet_helper, pet_payload):
    response = pet_helper.create(pet_payload)
    assert response.status_code == 200

    get_response = pet_helper.get(pet_payload["id"])
    assert get_response.status_code == 200
    assert get_response.json()["name"] == pet_payload["name"]

    pet_helper.delete(pet_payload["id"])


def test_delete_pet(pet_helper, pet_payload):
    pet_helper.create(pet_payload)

    delete_response = pet_helper.delete(pet_payload["id"])
    assert delete_response.status_code == 200

    get_response = pet_helper.get(pet_payload["id"])
    assert get_response.status_code == 404


def test_update_pet(pet_helper, created_pet):
    updated = {**created_pet, "name": "Barsuk"}

    put_response = pet_helper.update(updated)
    assert put_response.status_code == 200

    get_response = pet_helper.get(created_pet["id"])
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Barsuk"


def test_get_pets_by_status(pet_helper):
    response = pet_helper.find_by_status("available")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_get_nonexistent_pet(pet_helper):
    response = pet_helper.get(999_999_999)
    assert response.status_code == 404


def test_create_pet_with_empty_name(pet_helper, pet_payload):
    pet_payload["name"] = ""
    response = pet_helper.create(pet_payload)
    assert response.status_code == 200

    pet_helper.delete(pet_payload["id"])
