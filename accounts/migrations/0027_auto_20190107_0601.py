# Generated by Django 2.1.4 on 2019-01-07 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
        ('accounts', '0026_remove_dashboard_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dashboard',
            new_name='Account',
        ),
    ]
