# Generated by Django 5.1.2 on 2024-10-26 17:28

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_merge_20241027_0020"),
    ]

    operations = [
        migrations.AlterField(
            model_name="food",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]