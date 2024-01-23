import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.shortcuts import get_object_or_404


from loginapp.models import Certificate
certificate_exists = get_object_or_404(Certificate,name="maliko")
print(certificate_exists.name)
