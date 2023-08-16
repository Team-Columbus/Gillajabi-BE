from django.db import models

# Create your models here.

class CoffeeMenu(models.Model):
    menu_category = models.CharField(verbose_name = "메뉴카테고리", max_length = 30)
    name = models.CharField(verbose_name = "메뉴이름", max_length=30)
    price = models.IntegerField(verbose_name = "가격")
    image = models.ImageField(verbose_name = "이미지", upload_to='coffee_images/', null=True, blank=True)
    Detail_page = models.BooleanField(verbose_name = "상세페이지유무", default = False)
    explanation = models.CharField(verbose_name = "설명", max_length = 1000)
    type = models.CharField(verbose_name = "타입", max_length = 30)
    

    def __str__(self):
        return self.name

class MenuDetail(models.Model):
    option = models.CharField(verbose_name = "옵션이름", max_length=50)
    price = models.IntegerField(verbose_name = "옵션가격")
    image = models.ImageField(verbose_name = "옵션이미지", upload_to='option_images/', null=True, blank=True)
    # CoffeeMenu = models.ForeignKey(to=CoffeeMenu, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(verbose_name = "타입", max_length = 30)

    def __str__(self):
        return self.option
