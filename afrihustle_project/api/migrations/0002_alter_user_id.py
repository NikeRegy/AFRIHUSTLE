# Generated by Django 5.2 on 2025-04-16 15:14

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('1b0855ef-81a0-416d-8ce6-f8fee0de4809'), primary_key=True, serialize=False),
        ),
    ]
