# Generated by Django 2.1.4 on 2019-01-04 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20190104_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='paid',
        ),
        migrations.AddField(
            model_name='accounts',
            name='total_paid',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
