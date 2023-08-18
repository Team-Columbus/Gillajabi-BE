from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Train, Bus
from .serializers import Train_ticket, Bus_ticket

# 기차 출발역 리스트
# @api_view(['GET'])
# def get_start_train_list(request):
#     start_station = Train.objects.values('start_station').distinct()
    
#     start_station_serializer = Start_stationSerializer(start_station, many=True)
#     response_data = {
#         'start_station': start_station_serializer.data,
#     }
    
#     return Response(response_data)

# 기차 출발역 리스트
@api_view(['GET'])
def get_start_train_list(request):
    start_stations = Train.objects.values('start_station').distinct()
    station_names = [station['start_station'] for station in start_stations]
    
    response_data = {
        'stations': station_names,
    }
    
    return Response(response_data)




# 기차 도착역 리스트
@api_view(['GET'])
def get_arrive_train_list(request):
    arrive_stations = Train.objects.values('arrive_station').distinct()
    station_names = [station['arrive_station'] for station in arrive_stations]
    
    response_data = {
        'stations': station_names,
    }
    
    return Response(response_data)

# # 기차 출발역 검색
# class SearchStartStation(APIView):
#     def post(self, request, format=None):
#         search_query = request.data.get('start_station', '')

#         if search_query:
#             # 검색어를 사용하여 출발 역을 필터링 (이 예시에서는 역 이름에 대소문자를 무시하고 검색)
#             start_stations = Train.objects.filter(start_station__icontains=search_query)
#             serializer = Start_stationSerializer(start_stations, many=True)
#             return Response(serializer.data)
#         else:
#             return Response([])
        
# # 기차 도착역 검색
# class SearchArriveStation(APIView):
#     def post(self, request, format=None):
#         search_query = request.data.get('arrive_station', '')

#         if search_query:
#             # 검색어를 사용하여 출발 역을 필터링(이 예시에서는 역 이름에 대소문자를 무시하고 검색)
#             arrive_stations = Train.objects.filter(arrive_station__icontains=search_query)
#             serializer = Arrive_stationSerializer(arrive_stations, many=True)
#             return Response(serializer.data)
#         else:
#             return Response([])

# 기차 티켓
@api_view(['POST'])
def get_train_ticket(request):
    start_station_name = request.data['start_station']
    arrive_station_name = request.data['arrive_station']
    
    if start_station_name and arrive_station_name:
        train_ticket = Train.objects.filter(start_station=start_station_name, arrive_station=arrive_station_name)
    else:
        train_ticket = Train.objects.all()

    serializer = Train_ticket(train_ticket, many=True)
    return Response(serializer.data)


# 버스 도착 터미널 리스트
@api_view(['GET'])
def get_arrive_bus_list(request):
    arrive_terminal = Bus.objects.values('arrive_terminal').distinct()
    terminal_names = [terminal['arrive_terminal'] for terminal in arrive_terminal]
    
    response_data = {
        'terminal': terminal_names,
    }
    
    return Response(response_data)


# 버스 티켓
@api_view(['POST'])
def get_terminal_ticket(request):
    start_terminal_name = request.data['start_terminal']
    arrive_terminal_name = request.data['arrive_terminal']
    
    if start_terminal_name and arrive_terminal_name:
        bus_ticket = Bus.objects.filter(start_terminal=start_terminal_name, arrive_terminal=arrive_terminal_name)
    else:
        bus_ticket = Bus.objects.all()

    serializer = Bus_ticket(bus_ticket, many=True)
    return Response(serializer.data)