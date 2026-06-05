from helpers.expect import expect


def test_create_user(user_helper, user_payload):
    expect(user_helper.create(user_payload), code=200)
    user_helper.delete(user_payload["username"])


def test_get_user(user_helper, created_user):
    response = user_helper.get(created_user["username"])
    expect(response, code=200)
    assert response.json()["username"] == created_user["username"]


def test_update_user(user_helper, created_user):
    updated = {**created_user, "username": f"{created_user['username']}_upd"}
    expect(user_helper.update(created_user["username"], updated), code=200)

    response = user_helper.get(updated["username"])
    expect(response, code=200)
    assert response.json()["username"] == updated["username"]


def test_delete_user(user_helper, user_payload):
    user_helper.create(user_payload)
    expect(user_helper.delete(user_payload["username"]), code=200)
    expect(user_helper.get(user_payload["username"]), code=404, message="User not found")
