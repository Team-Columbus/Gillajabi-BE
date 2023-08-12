from django.db import models

class CGVMovie(models.Model):
    id = models.BigAutoField(primary_key=True)
    movie_poster = models.URLField()
    title = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    theater_house = models.CharField(max_length=255)
    theater_floor = models.CharField(max_length=255)
    

    def __str__(self):
        return self.title

class Detail(models.Model):
    seat_number = models.IntegerField()
    max_seat = models.IntegerField(default=100)
    start_time = models.CharField(verbose_name="영화시작시간", max_length=30)
    end_time = models.CharField(verbose_name="영화종료시간", max_length=30)
    movie = models.ForeignKey(to=CGVMovie, on_delete=models.CASCADE,related_name="detail")

    def __str__(self):
        return self.start_time
    



