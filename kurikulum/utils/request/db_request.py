from requests.auth import HTTPBasicAuth
import requests

BASE_URL = 'http://localhost/'

class DBRequest:
    def __init__(self, url, method, headers) -> None:
        self.url = BASE_URL + url
        self.method = method
        self.headers = headers
        self.payload = None
        self.__auth = HTTPBasicAuth("obe", "passwordobe")

    def set_payload(self, payload):
        self.payload = payload

    def make_request(self):
        response = requests.request(self.method, self.url, headers=self.headers, data=self.payload, auth=self.__auth)
        return response