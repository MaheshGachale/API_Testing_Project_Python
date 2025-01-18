# utils/api_client.py
import requests
from config.config import BASE_URL, HEADERS

class APIClient:
    def __init__(self, base_url=BASE_URL, headers=HEADERS):
        self.base_url = base_url
        self.headers = headers

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)
        return response

    def post(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, headers=self.headers, json=payload)
        return response

    def put(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, headers=self.headers, json=payload)
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.delete(url, headers=self.headers)
        return response
