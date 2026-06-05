class UserHelper:
    def __init__(self, api_client, base_url):
        self.client = api_client
        self.base_url = base_url

    def create(self, payload):
        return self.client.post(f"{self.base_url}/user", json=payload)

    def get(self, username):
        return self.client.get(f"{self.base_url}/user/{username}")

    def update(self, username, payload):
        return self.client.put(f"{self.base_url}/user/{username}", json=payload)

    def delete(self, username):
        return self.client.delete(f"{self.base_url}/user/{username}")
