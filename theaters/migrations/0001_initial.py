# Generated by Django 4.2.4 on 2023-08-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CGVMovie',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('movie_poster', models.ImageField(upload_to='movie_posters/')),
                ('title', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=255)),
                ('theater_house', models.CharField(max_length=255)),
                ('theater_floor', models.CharField(max_length=255)),
                ('seat_number', models.IntegerField()),
                ('max_seat', models.IntegerField(default=100)),
            ],
        ),
    ]