

def test_create_user(api_client, base_url, user_payload):
    response = api_client.post(f"{base_url}/user", json=user_payload)
    assert response.status_code == 200
    api_client.delete(f"{base_url}/user/{user_payload['username']}")


def test_get_user(api_client, base_url, created_user):
    response = api_client.get(f"{base_url}/user/{created_user['username']}")
    assert response.status_code == 200


def test_update_user(base_url, created_user, api_client):
    update_user = created_user.copy()
    update_user['username'] = "Test$7439%2"
    put_response = api_client.put(f"{base_url}/user/{created_user['username']}", json=update_user)
    assert put_response.status_code == 200
    get_response = api_client.get(f"{base_url}/user/{update_user['username']}")
    assert get_response.status_code == 200
    assert get_response.json()['username'] == update_user['username']


def test_delete_user(base_url, api_client):
    new_user = \
        {
            "id": 121,
            "username": "Test$7439%1",
            "firstName": "Test1",
            "lastName": "Tests1",
            "email": "Test74391@example.com",
            "password": "1245788956231",
            "phone": "123456791",
            "userStatus": 11
        }
    post_response = api_client.post(f"{base_url}/user", json=new_user)
    assert post_response.status_code == 200
    delet_user = api_client.delete(f"{base_url}/user/{new_user['username']}")
    assert delet_user.status_code == 200
    get_response = api_client.get(f"{base_url}/user/{new_user['username']}")
    assert get_response.status_code == 404


