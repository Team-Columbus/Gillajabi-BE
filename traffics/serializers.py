from rest_framework import serializers
from .models import Train, Bus

# 기차 출발
# class Start_stationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Train
#         fields = ['id', 'start_station']

# class Start_stationSerializer(serializers.Serializer):
#     stations = serializers.ListField(child=serializers.CharField())

#     def create(self, validated_data):
#         return validated_data


# # 기차 도착
# class Arrive_stationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Train
#         fields = ['id', 'arrive_station']

# 기차 티켓
class Train_ticket(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ['id', 'train_name','start_station','arrive_station','start_time','arrive_time','price']


# 버스 티켓
class Bus_ticket(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['id', 'start_time','required_time','company','rate','rest_seat']