# Generated by Django 5.1.4 on 2024-12-20 07:15

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_uuid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
