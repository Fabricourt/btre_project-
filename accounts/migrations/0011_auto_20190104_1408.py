# Generated by Django 2.1.4 on 2019-01-04 11:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20190104_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='paid_amount',
        ),
        migrations.AddField(
            model_name='accounts',
            name='totalamountpaid',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
