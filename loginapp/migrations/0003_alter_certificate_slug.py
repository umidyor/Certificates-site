# Generated by Django 5.0.1 on 2024-01-23 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_certificate_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='slug',
            field=models.CharField(max_length=300),
        ),
    ]
