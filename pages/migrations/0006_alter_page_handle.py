# Generated by Django 4.1.5 on 2023-01-27 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0005_page_delete_homepage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="page",
            name="handle",
            field=models.SmallIntegerField(
                blank=True,
                choices=[
                    (1, "Home"),
                    (2, "Home"),
                    (3, "Home"),
                    (4, "Home"),
                    (5, "Home"),
                ],
                null=True,
            ),
        ),
    ]