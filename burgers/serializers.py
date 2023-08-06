from rest_framework import serializers
from .models import Mcdonald, SetMenu


class McdonaldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mcdonald
        fields = "__all__"


class SetMenuBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetMenu
        fields = "__all__"


class SetMenuReturnSerializer(SetMenuBaseSerializer):
    class Meta(SetMenuBaseSerializer.Meta):
        fields = ["id", "menu_name", "image", "price", "calorie", "menu_size"]


class SingleMenuReturnSerializer(McdonaldSerializer):
    class Meta(McdonaldSerializer.Meta):
        fields = ["id", "menu_name", "image", "price", "calorie", "menu_size"]


class DrinkSelectSerializer(McdonaldSerializer):
    class Meta(McdonaldSerializer.Meta):
        fields = ["id", "menu_name", "image", "price", "calorie"]
