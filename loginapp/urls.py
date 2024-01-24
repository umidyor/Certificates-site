from django.urls import path
from .views import *


urlpatterns=[
    path('', get_name, name='certificates_name'),
    path('student/<str:slug>',view_certificate,name='user_ssl'),
    path('media/<path:file_path>', serve_media, name='serve_media'),
]
