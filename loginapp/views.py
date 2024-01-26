from django.shortcuts import render, redirect
from .models import Certificate
from django.urls import reverse
# Create your views here.
from django.http import FileResponse
from django.conf import settings
import os
from django.http import HttpResponse
from rest_framework import views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
def get_name(request):
    return render(request,"get_name.html")
def view_certificate(request, slug):
    form=get_object_or_404(Certificate,slug=slug)
    return render(request,"certificate.html",{'form':form})


def serve_media(request, file_path):
    # Build the absolute path to the requested media file
    file_path = os.path.join(settings.MEDIA_ROOT, file_path)

    # Check if the file exists
    if os.path.exists(file_path):
        # Serve the file using FileResponse
        response = FileResponse(open(file_path, 'rb'))
        return response
    else:
        # Handle file not found gracefully
        return HttpResponse("Error image serve_media")

from rest_framework import status
# class CertificateAPIView(views.APIView):
#     def post(self, request, *args,**kwargs):
#         name=request.data['name_input']
#         data = dict(status='not found')
#         check_name=Certificate.objects.filter(name=name)
#         if check_name.exists():
#             data['name_input'] = check_name[0].name
#             data['status'] = 'found'
#             data['url_redirect'] = 'http://127.0.0.1:8000/' + reverse('Certificate:user_ssl', kwargs={'name':check_name[0].name})
#             # return redirect(reverse('Certificate:user_ssl', kwargs={'name':check_name[0].name}))
#         else:
#             error_message = "Validation failed."
#             data['error_message'] = error_message
#         return Response(data, status=status.HTTP_200_OK)
        # return Response({'name_input':'Atabek'}, status=status.HTTP_200_OK)



from .forms import SearchCertificateForm
def get_name(request):
    form = SearchCertificateForm(request.GET)

    if form.is_valid():
        seria = form.cleaned_data['seria']
        sertificate_id = form.cleaned_data['sertificate_id']

        try:
            certificate_exists = Certificate.objects.get(seria=seria, sertificate_id=sertificate_id)
            context = {
                'form': form,
                'certificate_exists': certificate_exists,
            }
            return render(request, 'found.html', context)
        except Certificate.DoesNotExist:
            message="Ushbu sertifikat topilmadi yoki mavjud emas"
            return render(request, 'get_name.html', {'form': form,'message':message})

    return render(request, 'get_name.html', {'form': form})


def custom_404(request, exception):
    return render(request, '404.html', status=404)