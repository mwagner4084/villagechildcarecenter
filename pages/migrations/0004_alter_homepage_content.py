# Generated by Django 4.1.5 on 2023-01-27 02:10

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0003_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="content",
            field=tinymce.models.HTMLField(max_length=1000),
        ),
    ]
