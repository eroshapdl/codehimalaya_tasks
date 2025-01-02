# Generated by Django 5.1.4 on 2024-12-23 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0003_ticket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='event',
            new_name='event_details',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='ticket_number',
            new_name='ticket_uuid',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='purchase_date',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='user',
        ),
    ]
