from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', get_name, name='certificates_name'),
    path('student/<str:name>',view_certificate,name='user_ssl'),
    path('media/<path:file_path>', serve_media, name='serve_media'),
    path('api/certificate/', CertificateAPIView.as_view(), name='certificate_api'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)