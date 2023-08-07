from rest_framework import serializers
from .models import Mcdonald, DetailMenu


class McdonaldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mcdonald
        fields = "__all__"


class SideMenuReturnSerializer(McdonaldSerializer):
    adjusted_price = serializers.SerializerMethodField()

    def get_adjusted_price(self, obj):
        return obj.price - 2000

    class Meta(McdonaldSerializer.Meta):
        fields = ["id", "menu_name", "image", "adjusted_price", "calorie", "menu_size"]


class SingleMenuReturnSerializer(McdonaldSerializer):
    class Meta(McdonaldSerializer.Meta):
        fields = ["id", "menu_name", "image", "price", "calorie", "menu_size"]


class DrinkSelectSerializer(McdonaldSerializer):
    adjusted_price = serializers.SerializerMethodField()

    def get_adjusted_price(self, obj):
        return obj.price - 1700

    class Meta(McdonaldSerializer.Meta):
        fields = ["id", "menu_name", "image", "adjusted_price", "calorie"]


class DetailMenuBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailMenu
        fields = "__all__"


class DetailMenuReturnSerializer(DetailMenuBaseSerializer):
    class Meta(DetailMenuBaseSerializer.Meta):
        fields = ["id", "menu_name", "image", "price", "calorie", "menu_size"]
