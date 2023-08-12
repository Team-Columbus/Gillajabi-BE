from django.db import models

class Train(models.Model):
    id = models.BigAutoField(primary_key=True)
    train_name = models.CharField(max_length=255)
    start_station = models.CharField(max_length=255)
    arrive_station = models.CharField(max_length=255)
    start_time = models.CharField(max_length=255)
    arrive_time = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
   
    def __str__(self):
        return self.start_station
    
class Bus(models.Model):
    id = models.BigAutoField(primary_key=True)
    start_terminal = models.CharField(max_length=255,null=True, default='')
    arrive_terminal = models.CharField(max_length=255,null=True, default='')
    start_time = models.CharField(max_length=255)
    required_time = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    rate = models.CharField(max_length=255)
    rest_seat = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
   
    def __str__(self):
        return self.price