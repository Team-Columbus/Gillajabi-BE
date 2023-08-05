from django.db import models

class CGVMovie(models.Model):
    id = models.BigAutoField(primary_key=True)
    movie_poster = models.ImageField(upload_to='movie_posters/')
    title = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    theater_house = models.CharField(max_length=255)
    theater_floor = models.CharField(max_length=255)
    seat_number = models.IntegerField()
    max_seat = models.IntegerField(default=100)

    def __str__(self):
        return self.title
