# Generated by Django 4.1.5 on 2023-01-27 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0014_page_content2_alter_page_content"),
    ]

    operations = [
        migrations.RenameField(
            model_name="page",
            old_name="content2",
            new_name="content_secondary",
        ),
    ]
