# Generated by Django 2.1.4 on 2019-01-04 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_dashboard_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]
