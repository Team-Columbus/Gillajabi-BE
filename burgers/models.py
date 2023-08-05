from django.db import models

# Create your models here.


class Mcdonald(models.Model):
    menu_name = models.CharField(verbose_name="메뉴이름", max_length=30, null=False)
    image = models.URLField(verbose_name="메뉴이미지", max_length=500, null=True)
    price = models.IntegerField(verbose_name="가격")
    calorie = models.CharField(verbose_name="칼로리", max_length=30)
    menu_category = models.CharField(verbose_name="메뉴카테고리", max_length=30)
    food_category = models.CharField(verbose_name="음식카테고리", max_length=30, null=True)
    menu_size = models.CharField(
        verbose_name="사이즈", max_length=30, blank=True, null=True
    )
    is_set = models.BooleanField(verbose_name="세트여부")
    is_happy = models.BooleanField(verbose_name="해피스낵여부", default=False)

    def __str__(self):
        return self.menu_name


class SetMenu(models.Model):
    menu_name = models.CharField(verbose_name="메뉴이름", max_length=30, null=False)
    image = models.URLField(verbose_name="메뉴이미지", max_length=500, null=True)
    price = models.IntegerField(verbose_name="가격")
    calorie = models.CharField(verbose_name="칼로리", max_length=30)
    menu_size = models.CharField(
        verbose_name="사이즈", max_length=30, blank=True, null=True
    )
    single_menu = models.ForeignKey(
        to=Mcdonald, on_delete=models.CASCADE, related_name="set_menus"
    )

    def __str__(self):
        return self.menu_name
