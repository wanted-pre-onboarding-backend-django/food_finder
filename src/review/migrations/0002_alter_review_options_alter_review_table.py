# Generated by Django 5.0.7 on 2024-09-01 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("review", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="review",
            options={"verbose_name": "Review", "verbose_name_plural": "Reviews"},
        ),
        migrations.AlterModelTable(
            name="review",
            table="Review",
        ),
    ]