def expect(response, code=None, message=None):
    if code is not None:
        assert response.status_code == code, (
            f"Expected status {code}, got {response.status_code}. Body: {response.text}"
        )
    if message is not None:
        body = response.json()
        assert body.get("message") == message, (
            f"Expected message '{message}', got '{body.get('message')}'. Body: {response.text}"
        )
