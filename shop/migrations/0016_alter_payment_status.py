# Generated by Django 4.1.7 on 2023-03-03 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_orderitem_price_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('SUCCESS', 'SUCCESS'), ('FAILED', 'FAILED')], default='PENDING', max_length=50),
        ),
    ]