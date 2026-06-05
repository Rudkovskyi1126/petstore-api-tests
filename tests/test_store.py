def test_create_order(store_helper, order_payload):
    response = store_helper.create_order(order_payload)
    assert response.status_code == 200

    store_helper.delete_order(order_payload["id"])


def test_get_order(store_helper, created_order):
    response = store_helper.get_order(created_order["id"])
    assert response.status_code == 200
    assert response.json()["id"] == created_order["id"]


def test_delete_order(store_helper, created_order):
    delete_response = store_helper.delete_order(created_order["id"])
    assert delete_response.status_code == 200

    get_response = store_helper.get_order(created_order["id"])
    assert get_response.status_code == 404


def test_get_inventory(store_helper):
    response = store_helper.get_inventory()
    assert response.status_code == 200
