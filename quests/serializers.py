from rest_framework import serializers
from .models import Quest


class QuestReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ["content", "is_do", "is_accept"]
