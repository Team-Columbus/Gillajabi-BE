# Generated by Django 4.2.1 on 2023-08-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "theaters",
            "0003_remove_cgvmovie_max_seat_remove_cgvmovie_seat_number_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="detail",
            name="time",
        ),
        migrations.AddField(
            model_name="detail",
            name="end_time",
            field=models.CharField(default="", max_length=30, verbose_name="영화종료시간"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="detail",
            name="start_time",
            field=models.CharField(default="", max_length=30, verbose_name="영화시작시간"),
            preserve_default=False,
        ),
    ]
