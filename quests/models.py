from django.db import models
from users.models import User


# Create your models here.


class Quest(models.Model):

    content = models.JSONField(verbose_name="퀘스트내용",max_length=300, null=True,blank=True)
    is_do = models.BooleanField(verbose_name="퀘스트수행여부",default=False)
    is_accept = models.BooleanField(verbose_name="퀘스트수락여부",default=False)
    user = models.ForeignKey(to = User, on_delete=models.CASCADE,related_name="quest")
    
    