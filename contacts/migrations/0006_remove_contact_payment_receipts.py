# Generated by Django 2.1.4 on 2019-01-04 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20190104_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='payment_receipts',
        ),
    ]
