# Generated by Django 4.2.1 on 2023-08-03 05:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_user_email_alter_user_name_alter_user_password_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscribe",
            name="is_subscribe",
            field=models.BooleanField(default=False, verbose_name="구독여부"),
        ),
    ]
