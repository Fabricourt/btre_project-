# Generated by Django 2.1.4 on 2019-01-04 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_accounts_monthly_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='agreed_payment_plan',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
