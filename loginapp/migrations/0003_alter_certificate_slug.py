# Generated by Django 5.0.1 on 2024-01-19 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0002_alter_certificate_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='slug',
            field=models.CharField(blank=True, max_length=500, unique=True),
        ),
    ]
