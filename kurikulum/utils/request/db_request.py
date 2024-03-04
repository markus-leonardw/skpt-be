from requests.auth import HTTPBasicAuth
import requests


class DBRequest:
    def __init__(self, url, method, headers) -> None:
        self.url = url
        self.method = method
        self.headers = headers
        self.__auth = HTTPBasicAuth("admin", "admin")

    def set_payload(self, payload):
        self.payload = payload

    def make_request(self):
        response = requests.request(self.method, self.url, headers=self.headers, data=self.payload, auth=self.__auth)
        return response