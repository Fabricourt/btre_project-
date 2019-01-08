# Generated by Django 2.1.4 on 2019-01-04 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('photo_personal', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('email', models.CharField(max_length=100)),
                ('personalidnumber', models.CharField(max_length=100)),
                ('plot_number', models.CharField(blank=True, max_length=200)),
                ('plot_size', models.CharField(blank=True, max_length=50)),
                ('plot_Buying_price', models.CharField(blank=True, max_length=200)),
                ('payment_plan', models.CharField(blank=True, max_length=200)),
                ('deposit_amount', models.IntegerField()),
                ('amounttobepaid_monthly', models.IntegerField()),
                ('Balance', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('message', models.TextField(blank=True)),
                ('user_id', models.IntegerField()),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
            ],
        ),
    ]
