# Generated by Django 4.2.3 on 2023-11-06 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_cart_customer_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='order_date',
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
