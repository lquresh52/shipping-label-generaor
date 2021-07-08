# Generated by Django 3.2.5 on 2021-07-08 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=500)),
                ('phone_number', models.BigIntegerField()),
                ('falt_house_no_building_name', models.TextField()),
                ('street_colony', models.TextField()),
                ('pincode', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('landmark', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]