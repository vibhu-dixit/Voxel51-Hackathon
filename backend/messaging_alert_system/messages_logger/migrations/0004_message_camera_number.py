# Generated by Django 5.1.6 on 2025-02-15 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messages_logger', '0003_remove_message_alert_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='camera_number',
            field=models.IntegerField(default=1),
        ),
    ]
