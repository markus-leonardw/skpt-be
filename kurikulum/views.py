from requests.auth import HTTPBasicAuth
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import os
import json
from django.middleware import csrf

def read(request):
    url = "http://ec2-52-77-76-222.ap-southeast-1.compute.amazonaws.com:7200/repositories/obe"

    payload = {
        "query": """
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX OBE: <http://www.semanticweb.org/ami/ontologies/2024/0/OBE#>
            SELECT ?course WHERE {
                ?course rdf:type OBE:Course
            } LIMIT 5
        """,
        "infer": "true",
        "sameAs": "true",
        "limit": 1001,
        "offset": 0
    }

    headers = {
        'Accept': 'application/x-sparqlstar-results+json, application/sparql-results+json;q=0.9, */*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    
    GRAPHDB_USER = 'admin' # os.getenv('GRAPHDB_USER')
    GRAPHDB_PASSWORD = 'admin' # os.getenv('GRAPHDB_PASSWORD')

    response = requests.request("POST", url, headers=headers, data=payload, auth=HTTPBasicAuth(GRAPHDB_USER, GRAPHDB_PASSWORD))

    return HttpResponse(response.text, content_type='application/json')

# for dev use
def get_csrf_token(request):
    csrf_token = csrf.get_token(request)
    return HttpResponse(csrf_token)


def delete_subject(request):
    if request.POST:
        subject = request.POST['subject']

        url = "http://ec2-52-77-76-222.ap-southeast-1.compute.amazonaws.com:7200/rest/repositories/obe/sparql-templates/execute"

        payload = json.dumps({
            "templateId": "http://example.com/template#delete",
            "s": subject
        })

        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/json',
        }

        GRAPHDB_USER = 'admin' # os.getenv('GRAPHDB_USER')
        GRAPHDB_PASSWORD = 'admin' # os.getenv('GRAPHDB_PASSWORD')

        response = requests.request("POST", url, headers=headers, data=payload, auth=HTTPBasicAuth(GRAPHDB_USER, GRAPHDB_PASSWORD))

        return JsonResponse(response.text, status=200, safe=False)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


def update(request):
    pass

def insert(request):
    url = "http://ec2-52-77-76-222.ap-southeast-1.compute.amazonaws.com:7200/rest/repositories/obe/import/upload/text"

    payload = json.dumps({
        "name": "dummy3",
        "status": "DONE",
        "context": "default",
        "replaceGraphs": [],
        "forceSerial": False,
        "type": "text",
        "format": "text/turtle",
        "data": "PREFIX OBE: <http://www.semanticweb.org/ami/ontologies/2024/0/OBE#>\nPREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n\nOBE:course_markus rdf:type OBE:Course .",
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


    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=UTF-8',
    }

    GRAPHDB_USER = 'admin' # os.getenv('GRAPHDB_USER')
    GRAPHDB_PASSWORD = 'admin' # os.getenv('GRAPHDB_PASSWORD')


    response = requests.request("POST", url, headers=headers, data=payload, auth=HTTPBasicAuth(GRAPHDB_USER, GRAPHDB_PASSWORD))

    url = "http://ec2-52-77-76-222.ap-southeast-1.compute.amazonaws.com:7200/rest/repositories/obe/import/upload/status?remove=true"

    payload = "[\"dummy3\"]"
    response_delete = requests.request("DELETE", url, headers=headers, data=payload, auth=HTTPBasicAuth(GRAPHDB_USER, GRAPHDB_PASSWORD))

    return JsonResponse(response.text, safe=False)