# Generated by Django 2.1.4 on 2019-01-04 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20190104_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='amount_paid',
            new_name='paid_amount',
        ),
    ]
