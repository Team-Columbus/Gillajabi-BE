# Generated by Django 4.2.1 on 2023-08-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0014_alter_temporarystorage_save"),
    ]

    operations = [
        migrations.AlterField(
            model_name="temporarystorage",
            name="save",
            field=models.JSONField(default="{}", max_length=300, verbose_name="임시저장"),
        ),
    ]
