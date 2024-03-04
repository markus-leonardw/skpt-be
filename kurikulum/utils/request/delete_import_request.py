import json
from kurikulum.utils.request.db_request import DBRequest


class DeleteRequest(DBRequest):
    def __init__(self) -> None:
        url = "http://ec2-52-77-76-222.ap-southeast-1.compute.amazonaws.com:7200/rest/repositories/obe/import/upload/status?remove=true"
        method = "DELETE"
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json;charset=UTF-8',
        }
        
        super().__init__(url, method, headers)

    def generate_payload(self, name):
        payload = json.dumps([
            name
        ])
        
        return payload

    def set_payload(self, name):
        payload = self.generate_payload(name)
        super().set_payload(payload)

