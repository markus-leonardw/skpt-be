import json
from kurikulum.utils.request.db_request import DBRequest


class InsertRequest(DBRequest):
    def __init__(self) -> None:
        url = "rest/repositories/obe/import/upload/text"
        method = "POST"
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json;charset=UTF-8',
        }
        
        super().__init__(url, method, headers)

    def generate_payload(self, name, data):
        payload = json.dumps({
            "name": f"{name}",
            "status": "DONE",
            "context": "default",
            "replaceGraphs": [],
            "forceSerial": False,
            "type": "text",
            "format": "text/turtle",
            "data": f"{data}",
            "parserSettings": {
                "preserveBNodeIds": False,
                "failOnUnknownDataTypes": False,
                "verifyDataTypeValues": False,
                "normalizeDataTypeValues": False,
                "failOnUnknownLanguageTags": False,
                "verifyLanguageTags": True,
                "normalizeLanguageTags": False,
                "stopOnError": True
            }
        })

        return payload

    def set_payload(self, name, data):
        payload = self.generate_payload(name, data)
        super().set_payload(payload)

