# Generated by Django 4.1 on 2022-09-10 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0004_remove_customer_country_remove_customer_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]