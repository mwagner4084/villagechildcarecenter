# Generated by Django 4.1.5 on 2023-02-03 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0020_contact_subscriber"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Subscriber",
            new_name="InformationRequest",
        ),
    ]