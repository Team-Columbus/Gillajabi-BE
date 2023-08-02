from datetime import datetime
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, user_id, password=None, name=None, birth=None):
        if not user_id:
            raise ValueError("사용자 아이디는 필수입니다.")

        
        user = self.model(user_id=user_id, name=name, birth=birth)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password=None, name=None, birth=None):
        user = self.create_user(user_id, password, name, birth)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    user_id = models.CharField(
        unique=True, verbose_name="아이디", max_length=30, null=False, blank=False
    )
    password = models.CharField(
        verbose_name="비밀번호", max_length=30, null=False, blank=False
    )

    name = models.CharField(verbose_name="이름", max_length=30, default="")
    birth = models.DateField(verbose_name="생일", max_length=30, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "user_id"
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.user_id

class Subscribe(models.Model):
    
    is_subscribe = models.BooleanField(default=False)
    sub_start = models.DateTimeField(verbose_name="구독시작날짜",null=True, blank=True, default=None)
    sub_end = models.DateTimeField(verbose_name="구독만료날짜",null=True, blank=True, default=None)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="subscribe")
    
    def __str__(self):
        return self.is_subscribe
    