from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import User, Subscribe


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token = super().get_token(user)
        
        
        return token


class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
class UserInfoReturnSerializer(UserBaseSerializer):
    
    class Meta(UserBaseSerializer.Meta):
        
        fields=["name","birth"]

class SubscribeBaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subscribe
        fields = ["is_subscribe","sub_start","sub_end"]
        