from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_csrf_token),
    path('read', views.read),
    path('delete', views.delete_subject),
    path('insert', views.insert)
]