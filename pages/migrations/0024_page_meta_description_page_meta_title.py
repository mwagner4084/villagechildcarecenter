# Generated by Django 4.1.5 on 2023-11-03 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0023_alter_page_handle"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="meta_description",
            field=models.TextField(default="Default meta description"),
        ),
        migrations.AddField(
            model_name="page",
            name="meta_title",
            field=models.CharField(default="Default meta title", max_length=255),
        ),
    ]
