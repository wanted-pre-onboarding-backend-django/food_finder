# Generated by Django 5.0.7 on 2024-08-30 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0002_alter_restaurant_category"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="restaurant",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="unique_code",
            field=models.CharField(
                default=1234567890,
                max_length=64,
                unique=True,
                verbose_name="SHA-256 Hash Value",
            ),
            preserve_default=False,
        ),
    ]