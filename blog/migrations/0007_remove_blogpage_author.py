# Generated by Django 4.2.16 on 2024-10-06 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_blogpage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogpage",
            name="author",
        ),
    ]
