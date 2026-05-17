import requests

def test_create_and_get_pet(base_url):
    new_pet = \
    {
        "id": 127,
        "name": "Bars",
        "status": "available",
        "photoUrls": ["https://pet.barsik.com"]
    }
    post_response = requests.post(f"{base_url}/pet", json=new_pet)
    assert post_response.status_code == 200
    get_response = requests.get(f"{base_url}/pet/127")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Bars"


def test_delete_pet(base_url):
    new_pet = \
        {
            "id": 12,
            "name": "Barsik",
            "status": "available",
            "photoUrls": ["https://pet.barsik.com"]
        }
    post_response = requests.post(f"{base_url}/pet", json=new_pet)
    assert post_response.status_code == 200
    delete_response = requests.delete(f"{base_url}/pet/12")
    assert delete_response.status_code == 200
    get_response = requests.get(f"{base_url}/pet/12")
    assert get_response.status_code == 404


def test_update_pet(base_url):

    new_pet = \
        {
            "id": 127,
            "name": "Bars",
            "status": "available"
        }
    post_response = requests.post(f"{base_url}/pet", json=new_pet)
    assert post_response.status_code == 200

    update_pet = \
    {
        "id": 127,
        "name": "Barsuk",
    }
    put_response = requests.put(f"{base_url}/pet", json=update_pet)
    assert put_response.status_code == 200
    get_response = requests.get(f"{base_url}/pet/127")
    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Barsuk"


def test_get_pets_by_status(base_url):
    get_response = requests.get(f"{base_url}/pet/findByStatus", params={"status": "available"})
    assert get_response.status_code == 200
    assert len(get_response.json()) > 0
