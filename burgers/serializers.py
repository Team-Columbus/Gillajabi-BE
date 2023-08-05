from rest_framework import serializers
from .models import Mcdonald,SetMenu


class McdonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mcdonald
        fields = "__all__"

class SetMenuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SetMenu
        fields = "__all__"