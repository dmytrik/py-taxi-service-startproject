# Generated by Django 5.1.3 on 2024-11-07 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taxi", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="driver",
            options={"verbose_name": "driver", "verbose_name_plural": "drivers"},
        ),
    ]
