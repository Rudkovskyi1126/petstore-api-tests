def expect(response, code=None, message=None, reason=None):
    prefix = f"[{reason}] " if reason else ""

    if code is not None:
        assert response.status_code == code, (
            f"{prefix}Expected status {code}, got {response.status_code}. Body: {response.text}"
        )
    if message is not None:
        body = response.json()
        assert body.get("message") == message, (
            f"{prefix}Expected message '{message}', got '{body.get('message')}'. Body: {response.text}"
        )
