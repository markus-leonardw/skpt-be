import json
from kurikulum.utils.request.db_request import DBRequest


class ReadRequest(DBRequest):
    def __init__(self) -> None:
        url = "http://ec2-52-77-76-222.ap-southeast-1.compute.amazonaws.com:7200/repositories/obe"
        method = "POST"
        headers = {
            'Accept': 'application/x-sparqlstar-results+json, application/sparql-results+json;q=0.9, */*;q=0.8',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        
        super().__init__(url, method, headers)

    def generate_payload(self, query):
        payload = {
            "query": f"{query}",
            "infer": "true",
            "sameAs": "true",
            "limit": 1001,
            "offset": 0
        }
        
        return payload

    def set_payload(self, query):
        payload = self.generate_payload(query)
        super().set_payload(payload)

