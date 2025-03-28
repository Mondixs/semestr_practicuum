# Generated by Django 5.1.7 on 2025-03-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
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
                (
                    "gender",
                    models.CharField(
                        choices=[("Male", "Male"), ("Female", "Female")], max_length=10
                    ),
                ),
                ("age", models.IntegerField()),
                ("city", models.CharField(max_length=100)),
                ("academic_pressure", models.FloatField()),
                ("study_satisfaction", models.FloatField()),
            ],
        ),
    ]
