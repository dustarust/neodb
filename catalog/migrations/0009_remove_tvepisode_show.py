# Generated by Django 3.2.19 on 2023-06-19 23:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0008_delete_historicalitem"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tvepisode",
            name="show",
        ),
    ]
