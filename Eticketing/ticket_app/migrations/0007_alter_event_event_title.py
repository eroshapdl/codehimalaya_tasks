# Generated by Django 4.2.17 on 2024-12-31 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0006_ticket_status_ticket_ticket_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
