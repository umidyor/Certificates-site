from django.db import models
from django.utils.text import slugify
# Create your models here.
class Certificate(models.Model):
    certificate = models.ImageField(upload_to="uploads/")
    name = models.CharField(max_length=500,unique=True)
    slug = models.CharField(max_length=500, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name+"astrum-certificate-uz")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

