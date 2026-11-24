import requests


class ApiClient:
    def __init__(self, base_url="https://jsonplaceholder.typicode.com", timeout=10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json; charset=UTF-8"})

    def get(self, path, params=None):
        return self.session.get(f"{self.base_url}{path}", params=params, timeout=self.timeout)

    def post(self, path, payload):
        return self.session.post(f"{self.base_url}{path}", json=payload, timeout=self.timeout)

    def put(self, path, payload):
        return self.session.put(f"{self.base_url}{path}", json=payload, timeout=self.timeout)

    def delete(self, path):
        return self.session.delete(f"{self.base_url}{path}", timeout=self.timeout)
