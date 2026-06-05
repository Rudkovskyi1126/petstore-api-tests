from helpers.expect import expect


def test_create_user(user_helper, user_payload):
    expect(user_helper.create(user_payload), code=200,
           reason="Creating a new user should return 200")
    user_helper.delete(user_payload["username"])


def test_get_user(user_helper, created_user):
    response = user_helper.get(created_user["username"])
    expect(response, code=200,
           reason="Fetching an existing user by username should return 200")
    assert response.json()["username"] == created_user["username"], (
        "Username in response should match the username used to fetch it"
    )


def test_update_user(user_helper, created_user):
    updated = {**created_user, "username": f"{created_user['username']}_upd"}
    expect(user_helper.update(created_user["username"], updated), code=200,
           reason="Updating an existing user should return 200")
    response = user_helper.get(updated["username"])
    expect(response, code=200,
           reason="Fetching the updated user by new username should return 200")
    assert response.json()["username"] == updated["username"], (
        "Username in response should reflect the value sent in the update request"
    )


def test_delete_user(user_helper, user_payload):
    user_helper.create(user_payload)
    expect(user_helper.delete(user_payload["username"]), code=200,
           reason="Deleting an existing user should return 200")
    expect(user_helper.get(user_payload["username"]), code=404, message="User not found",
           reason="Fetching a deleted user should return 404")
