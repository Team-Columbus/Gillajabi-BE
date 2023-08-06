from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import McdonaldSerializer,SetMenuReturnSerializer,DrinkSelectSerializer
from .models import Mcdonald

# Create your views here.


class MenuListView(APIView):
    def post(self, request):
        menu_category = request.data["menu_category"]

        if menu_category == "해피 스낵":
            data = Mcdonald.objects.filter(is_happy=True)
        else:
            data = Mcdonald.objects.filter(menu_category=menu_category)
        serilaizer = McdonaldSerializer(data, many=True)
        return Response(serilaizer.data)


class SetMenuListView(APIView):
    def post(self, request):
        menu_name = request.data["menu_name"]
        menu = Mcdonald.objects.get(menu_name=menu_name)

        serilaized_pets = SetMenuReturnSerializer(menu.set_menus.all(), many=True).data

        return Response(serilaized_pets)


class SideMenuListView(APIView):
    def get(self, request):
        data = Mcdonald.objects.filter(
            Q(menu_name__contains="후라이") | Q(menu_name__contains="코울슬로")
        )

        serialized_data = McdonaldSerializer(data, many=True).data
        return Response(serialized_data)
    
    
class DrinkListView(APIView):
    
    def get(self,request):
        
        data = Mcdonald.objects.filter(menu_category="음료")
        
        serialized_data = DrinkSelectSerializer(data,many=True).data
        
        return Response(serialized_data)
