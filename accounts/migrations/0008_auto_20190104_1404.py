# Generated by Django 2.1.4 on 2019-01-04 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190104_1401'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='agreed_payment_plan',
            new_name='payment_schedule',
        ),
    ]
