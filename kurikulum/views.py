from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import os
import json

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

def read(request):
    import requests

    url = 'http://localhost:7200/repositories/starwars'

    headers = {
        'Accept': 'application/x-sparqlstar-results+json, application/sparql-results+json;q=0.9, */*;q=0.8',
        'Accept-Language': 'en-US,en',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'http://localhost:7200',
        'Pragma': 'no-cache',
        'Referer': 'http://localhost:7200/sparql',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-GPC': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'X-GraphDB-Catch': '1000; throw',
        'X-GraphDB-Repository': 'starwars',
        'X-GraphDB-Repository-Location': '',
        'X-GraphDB-Track-Alias': 'query-editor-659336-1705835170684',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'Windows'
    }

    data = 'query=SELECT+%3Fmovie+%3FmovieName+%3FmovieReleaseDate+WHERE+%7B%0A++%3Chttps%3A%2F%2Fswapi.co%2Fvocabulary%2FHuman%3E+%3Chttps%3A%2F%2Fswapi.co%2Fvocabulary%2Ffilm%3E+%3Fmovie+.%0A++%3Fmovie+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23label%3E+%3FmovieName+%3B%0A+++++++++%3Chttps%3A%2F%2Fswapi.co%2Fvocabulary%2FreleaseDate%3E+%3FmovieReleaseDate+.%0A%7D+ORDER+BY+%3FmovieReleaseDate&infer=true&sameAs=true&limit=1001&offset=0'

    response = requests.post(url, headers=headers, data=data)

    print(response.text)
    return JsonResponse(response.text, safe=False)
