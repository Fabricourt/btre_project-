# Generated by Django 2.1.4 on 2018-12-28 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_listing_sqft'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='payment_plan',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
