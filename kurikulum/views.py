from datetime import datetime
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
    mapper = Mapper()
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
    mapper = Mapper()
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
            save_path = os.path.join(settings.STATIC_ROOT, f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}_{uploaded_file.name}")
            # Save the uploaded file
            with open(save_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            # Optionally, do something with the uploaded file
            # Redirect or render a response
            return render(request, 'upload_success.html')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
