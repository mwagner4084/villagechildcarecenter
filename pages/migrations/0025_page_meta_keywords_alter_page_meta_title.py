# Generated by Django 4.1.5 on 2023-11-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0024_page_meta_description_page_meta_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="meta_keywords",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="page",
            name="meta_title",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
