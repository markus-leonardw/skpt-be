import json
from kurikulum.utils.request.db_request import DBRequest


class GetQueryRequest(DBRequest):
  def __init__(self, name = None) -> None:
    url = f"rest/sparql/saved-queries?owner=obe{'' if name is None else f'&name={name}'}"
    method = "GET"
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json;charset=UTF-8',
    }
    
    super().__init__(url, method, headers)

