import json
from kurikulum.utils.request.db_request import DBRequest


class ExecuteTemplateRequest(DBRequest):
    def __init__(self) -> None:
        url = "http://ec2-52-77-76-222.ap-southeast-1.compute.amazonaws.com:7200/rest/repositories/obe/sparql-templates/execute"
        method = "POST"
        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
        }
        
        super().__init__(url, method, headers)

    def generate_payload(self, template_name, param):
        data = param.copy()
        data["templateId"] = f"http://example.com/template#{template_name}"

        payload = json.dumps(data)
        
        return payload

    def set_payload(self, template_name, param):
        payload = self.generate_payload(template_name, param)
        super().set_payload(payload)

