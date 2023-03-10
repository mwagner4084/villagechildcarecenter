# Generated by Django 4.1.5 on 2023-01-27 02:32

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0004_alter_homepage_content"),
    ]

    operations = [
        migrations.CreateModel(
            name="Page",
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
                ("handle", models.CharField(max_length=200)),
                ("title", models.CharField(max_length=200)),
                ("content", tinymce.models.HTMLField(max_length=1000)),
            ],
        ),
        migrations.DeleteModel(
            name="Homepage",
        ),
    ]
