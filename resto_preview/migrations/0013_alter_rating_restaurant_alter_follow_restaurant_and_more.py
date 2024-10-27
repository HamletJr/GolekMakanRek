# Generated by Django 5.1.2 on 2024-10-27 00:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_remove_restaurant_followers"),
        ("resto_preview", "0012_show_resto_alter_follow_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rating",
            name="restaurant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.restaurant"
            ),
        ),
        migrations.AlterField(
            model_name="follow",
            name="restaurant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="main.restaurant"
            ),
        ),
        migrations.DeleteModel(
            name="show_resto",
        ),
    ]