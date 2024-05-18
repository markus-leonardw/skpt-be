from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test),
    path('', views.get_csrf_token),
    path('read', views.read),
    path('delete', views.delete_subject),
    path('insert', views.insert),
    path('download', views.download_template_display),
    path('upload', views.upload_file),
    path('download_template', views.download_template, name='download_template'),
    path('validasi', views.validasi_page)
]