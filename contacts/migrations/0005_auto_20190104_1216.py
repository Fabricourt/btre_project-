# Generated by Django 2.1.4 on 2019-01-04 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_contact_reciepts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='reciepts',
            new_name='payment_receipts',
        ),
    ]
