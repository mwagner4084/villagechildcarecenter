# Generated by Django 4.1.5 on 2023-01-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0009_alter_page_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
