class PetHelper:
    def __init__(self, api_client, base_url):
        self.client = api_client
        self.base_url = base_url

    def create(self, payload):
        return self.client.post(f"{self.base_url}/pet", json=payload)

    def get(self, pet_id):
        return self.client.get(f"{self.base_url}/pet/{pet_id}")

    def update(self, payload):
        return self.client.put(f"{self.base_url}/pet", json=payload)

    def delete(self, pet_id):
        return self.client.delete(f"{self.base_url}/pet/{pet_id}")

    def find_by_status(self, status):
        return self.client.get(f"{self.base_url}/pet/findByStatus", params={"status": status})
