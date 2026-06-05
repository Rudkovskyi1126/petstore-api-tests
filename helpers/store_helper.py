class StoreHelper:
    def __init__(self, api_client, base_url):
        self.client = api_client
        self.base_url = base_url

    def create_order(self, payload):
        return self.client.post(f"{self.base_url}/store/order", json=payload)

    def get_order(self, order_id):
        return self.client.get(f"{self.base_url}/store/order/{order_id}")

    def delete_order(self, order_id):
        return self.client.delete(f"{self.base_url}/store/order/{order_id}")

    def get_inventory(self):
        return self.client.get(f"{self.base_url}/store/inventory")
