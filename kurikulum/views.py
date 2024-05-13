from datetime import datetime
import json
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.middleware import csrf
from django.http import FileResponse
import os
from kurikulum.utils.mapper.mapper_service import Mapper
from kurikulum.utils.request.delete_import_request import DeleteRequest
from kurikulum.utils.request.execute_template_request import ExecuteTemplateRequest
from kurikulum.utils.request.get_all_stored_query_request import GetQueryRequest
from kurikulum.utils.request.insert_import_request import InsertRequest
from kurikulum.utils.request.sparql_query_request import ReadRequest
from .forms import UploadFileForm

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

def execute_query(query):
    read_request = ReadRequest()
    read_request.set_payload(query)
    response = read_request.make_request()
    
    return json.loads(response.text)

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
    mapper = Mapper('dummy')
    ret = mapper.get_curriculum_data()
    insert_query = mapper.construct_insert_query(ret)

    import_name = "test_dummy_1"

    insert_request = InsertRequest()
    insert_request.set_payload(import_name, insert_query)

    response_insert = insert_request.make_request()

    delete_request = DeleteRequest()
    delete_request.set_payload(import_name)

    response_delete = delete_request.make_request()

    return JsonResponse(response_insert.text, safe=False)

def test(request):
    mapper = Mapper('dummy')
    ret = mapper.get_course_data()
    print(mapper.construct_insert_query(ret))
    return HttpResponse(mapper.construct_insert_query(ret))

def download_template(request):
    template_path = './static/bulk_insert_template.xlsx'
    return FileResponse(open(template_path, 'rb'), as_attachment=True)

def download_template_display(request):
    return render(request, 'download.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['file']
            # Define the path to save the uploaded file
            save_path = os.path.join(settings.STATIC_ROOT, "deleteafter.xlsx")
            # Save the uploaded file
            with open(save_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
                import_file_to_db(save_path)

            # Redirect or render a response
            return render(request, 'upload_success.html')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def import_file_to_db(file_path):
    mapper = Mapper(file_path)

    query_dict = mapper.construct_all_data()

    for class_name, query in query_dict.items():
        import_name = class_name + '_' + str(datetime.now()).replace(' ', '_')

        insert_request = InsertRequest()
        insert_request.set_payload(import_name, query)

        response_insert = insert_request.make_request()
        print("response insert:", response_insert.content)

        # delete uploaded query
        delete_request = DeleteRequest()
        delete_request.set_payload(import_name)

        response_delete = delete_request.make_request()

    # Delete the file since it is no longer needed
    mapper = None
    try:
        os.remove(file_path)
    except OSError as e:
        # expected
        pass

def validasi_page(request):
    queries = get_saved_queries()
    context = {
        'queries': queries
    }
    if request.method == 'POST':
        query_name = request.POST.get('dropdown')
        query = get_saved_queries(query_name)['body']
        print(query)
        result = execute_query(query)

        head = result['head']['vars']
        bindings = result['results']['bindings']

        context['head'] = head

        data = []
        for row in bindings:
            data.append([])
            for col in head:
                data[-1].append(row[col] if col in row else '')
        
        context['data'] = data

        return render(request, 'validasi.html', context)
    
    return render(request, 'validasi.html', context)

def get_saved_queries(name = None):
    get_query_request = GetQueryRequest(name)
    response = get_query_request.make_request()

    return json.loads(response.text)