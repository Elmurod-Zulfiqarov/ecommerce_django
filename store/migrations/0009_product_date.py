# Generated by Django 4.0.4 on 2022-04-25 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_order_address_alter_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
