# Generated by Django 4.2.17 on 2025-01-08 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0014_alter_ticket_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='payment_method',
            field=models.CharField(default='Khalti'),
        ),
    ]
