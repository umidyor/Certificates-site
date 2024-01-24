from django.db import models
from django.utils.text import slugify
from PIL import Image

class Certificate(models.Model):
    certificate = models.ImageField(upload_to="uploads/")
    certificate2 = models.ImageField(upload_to='uploads/')
    CATEGORY_CHOICES = [
        ('MK', 'MK'),
        ('DS', 'DS'),
        ('SF', 'SF'),
        ('FS', 'FS'),
        ('BD', 'BD'),
        ('FD', 'FD'),
        ('CS', 'CS'),
        ('3D', '3D'),
        ('NA', 'NA'),
    ]
    seria = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    sertificate_id = models.CharField(max_length=300)
    slug = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.seria}{self.sertificate_id}"


    def resize_image(self, image_path, target_size):
        image = Image.open(image_path)
        image = image.resize(target_size, Image.ANTIALIAS)
        image.save(image_path)
    def resize_images(self):
        # Set the desired size for the images
        target_size = (3072, 2008)

        # Resize the first image (certificate)
        self.resize_image(self.certificate.path, target_size)

        # Resize the second image (certificate2)
        self.resize_image(self.certificate2.path, target_size)

