# Generated by Django 4.2.17 on 2025-01-03 05:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0010_event_original_event_capacity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='original_event_capacity',
            new_name='original_capacity',
        ),
    ]
