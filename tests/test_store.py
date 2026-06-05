from helpers.expect import expect


def test_create_order(store_helper, order_payload):
    expect(store_helper.create_order(order_payload), code=200)
    store_helper.delete_order(order_payload["id"])


def test_get_order(store_helper, created_order):
    response = store_helper.get_order(created_order["id"])
    expect(response, code=200)
    assert response.json()["id"] == created_order["id"]


def test_delete_order(store_helper, created_order):
    expect(store_helper.delete_order(created_order["id"]), code=200)
    expect(store_helper.get_order(created_order["id"]), code=404, message="Order not found")


def test_get_inventory(store_helper):
    expect(store_helper.get_inventory(), code=200)
