# Generated by Django 2.1.4 on 2019-01-04 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='description',
        ),
    ]
