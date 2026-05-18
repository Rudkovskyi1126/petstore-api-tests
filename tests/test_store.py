import requests


def test_create_order(base_url):
    new_order =\
        {
            "id": 11,
            "petId": 127,
            "quantity": 1,
            "shipDate": "2026-05-17T11:36:00.229Z",
            "status": "placed",
            "complete": True
        }
    post_request = requests.post(f'{base_url}/store/order', json=new_order)
    assert post_request.status_code == 200


def test_get_order(base_url):
    new_order = \
        {
            "id": 12,
            "petId": 128,
            "quantity": 2,
            "shipDate": "2026-05-17T11:36:00.229Z",
            "status": "placed",
            "complete": True
        }
    post_request = requests.post(f'{base_url}/store/order', json=new_order)
    assert post_request.status_code == 200
    get_request = requests.get(f'{base_url}/store/order/{new_order["id"]}')
    assert get_request.status_code == 200


def test_delete_order(base_url):
    new_order = \
        {
            "id": 12,
            "petId": 128,
            "quantity": 2,
            "shipDate": "2026-05-17T11:36:00.229Z",
            "status": "placed",
            "complete": True
        }
    post_request = requests.post(f'{base_url}/store/order', json=new_order)
    assert post_request.status_code == 200
    delete_request = requests.delete(f'{base_url}/store/order/{new_order["id"]}')
    assert delete_request.status_code == 200
    get_request = requests.get(f'{base_url}/store/order/{new_order["id"]}')
    assert get_request.status_code == 404


def test_get_inventory(base_url):
    get_request = requests.get(f'{base_url}/store/inventory')
    assert get_request.status_code == 200



