# Generated by Django 2.1.4 on 2019-01-04 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
