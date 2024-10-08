# Generated by Django 4.2.1 on 2024-09-17 06:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FoodItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("calories", models.CharField(default="Not available", max_length=100)),
                ("fat_total_g", models.FloatField(blank=True, null=True)),
                ("fat_saturated_g", models.FloatField(blank=True, null=True)),
                ("protein", models.CharField(default="Not available", max_length=100)),
                ("sodium_mg", models.FloatField(blank=True, null=True)),
                ("potassium_mg", models.FloatField(blank=True, null=True)),
                ("cholesterol_mg", models.FloatField(blank=True, null=True)),
                ("carbohydrates_total_g", models.FloatField(blank=True, null=True)),
                ("fiber_g", models.FloatField(blank=True, null=True)),
                ("sugar_g", models.FloatField(blank=True, null=True)),
                ("date", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
