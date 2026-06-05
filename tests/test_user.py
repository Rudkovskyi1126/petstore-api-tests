def test_create_user(user_helper, user_payload):
    response = user_helper.create(user_payload)
    assert response.status_code == 200

    user_helper.delete(user_payload["username"])


def test_get_user(user_helper, created_user):
    response = user_helper.get(created_user["username"])
    assert response.status_code == 200
    assert response.json()["username"] == created_user["username"]


def test_update_user(user_helper, created_user):
    updated = {**created_user, "username": f"{created_user['username']}_upd"}

    put_response = user_helper.update(created_user["username"], updated)
    assert put_response.status_code == 200

    get_response = user_helper.get(updated["username"])
    assert get_response.status_code == 200
    assert get_response.json()["username"] == updated["username"]


def test_delete_user(user_helper, user_payload):
    user_helper.create(user_payload)

    delete_response = user_helper.delete(user_payload["username"])
    assert delete_response.status_code == 200

    get_response = user_helper.get(user_payload["username"])
    assert get_response.status_code == 404
