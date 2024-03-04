from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware import csrf
from kurikulum.utils.request.delete_import_request import DeleteRequest
from kurikulum.utils.request.execute_template_request import ExecuteTemplateRequest
from kurikulum.utils.request.insert_import_request import InsertRequest
from kurikulum.utils.request.sparql_query_request import ReadRequest

def read(request):
    query = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX OBE: <http://www.semanticweb.org/ami/ontologies/2024/0/OBE#>
SELECT ?course WHERE {
    ?course rdf:type OBE:Course
} LIMIT 5
"""
    read_request = ReadRequest()
    read_request.set_payload(query)
    response = read_request.make_request()
    
    return HttpResponse(response.text, content_type='application/json')

# for dev use
def get_csrf_token(request):
    csrf_token = csrf.get_token(request)
    return HttpResponse(csrf_token)

@csrf_exempt
def delete_subject(request):
    if request.POST:
        subject = request.POST['subject']

        param = {
            "s": subject
        }

        execute_template_request = ExecuteTemplateRequest()
        execute_template_request.set_payload("delete", param)

        response = execute_template_request.make_request()

        return JsonResponse(response.text, status=200, safe=False)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def insert(request):
    data = """
PREFIX OBE: <http://www.semanticweb.org/ami/ontologies/2024/0/OBE#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
OBE:course_markus_2 rdf:type OBE:Course .
"""

    import_name = "test_dummy"

    insert_request = InsertRequest()
    insert_request.set_payload(import_name, data)

    response_insert = insert_request.make_request()

    delete_request = DeleteRequest()
    delete_request.set_payload(import_name)

    response_delete = delete_request.make_request()

    return JsonResponse(response_insert.text, safe=False)