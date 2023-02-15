# Generated by Django 3.0.3 on 2020-03-02 21:13

from django.db import migrations
from django.contrib.auth.models import User


def create_user(apps, schema_editor):
    User.objects.create_superuser("test", password="test")


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_user)
    ]
