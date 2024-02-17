from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import os
import json

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def read(request):
    url = "http://ec2-52-77-76-222.ap-southeast-1.compute.amazonaws.com:7200/repositories/obe"

    payload = "query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0APREFIX+OBE%3A+%3Chttp%3A%2F%2Fwww.semanticweb.org%2Fami%2Fontologies%2F2024%2F0%2FOBE%23%3E%0Aselect+%3Fcourse+where+%7B+%0A%09%3Fcourse+rdf%3Atype+OBE%3ACourse%0A%7D+limit+100+%0A&infer=true&sameAs=true&limit=1001&offset=0"
    headers = {
    'Accept': 'application/x-sparqlstar-results+json, application/sparql-results+json;q=0.9, */*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'http://ec2-52-77-76-222.ap-southeast-1.compute.amazonaws.com:7200',
    'Pragma': 'no-cache',
    'Referer': 'http://ec2-52-77-76-222.ap-southeast-1.compute.amazonaws.com:7200/sparql',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
    'X-GraphDB-Catch': '1000; throw',
    'X-GraphDB-Repository': 'obe',
    'X-GraphDB-Repository-Location': '',
    'X-GraphDB-Track-Alias': 'query-editor-42470-1708194968307',
    'X-Requested-With': 'XMLHttpRequest'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
    return HttpResponse(response.text, content_type='application/json')
