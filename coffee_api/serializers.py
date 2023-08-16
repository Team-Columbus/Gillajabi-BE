from rest_framework import serializers
from .models import CoffeeMenu
from .models import MenuDetail

class CoffeeMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMenu
        fields = "__all__"


class CoffeExplanationSerializer(CoffeeMenuSerializer):
    class Meta(CoffeeMenuSerializer.Meta):
        fields = ["name","price","image","explanation","type"]
    

class MenuDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuDetail
        fields = "__all__"