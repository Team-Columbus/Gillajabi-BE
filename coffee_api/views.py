from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CoffeeMenu
from .models import MenuDetail
from .serializers import CoffeeMenuSerializer,CoffeExplanationSerializer,MenuDetailSerializer


class CoffeeMenuListCreateView(generics.ListCreateAPIView):
    queryset = CoffeeMenu.objects.all()
    serializer_class = CoffeeMenuSerializer

class DetailSerializerListCreateView(generics.ListCreateAPIView):
   queryset = MenuDetail.objects.all()
   serializer_class = MenuDetailSerializer

class DetailOptionView(APIView):

    def post(self,request):
        
        menu_name = request.data["menu_name"]
        menu_type = request.data["type"]

        menu = CoffeeMenu.objects.get(name=menu_name)
        options = MenuDetail.objects.filter(type=menu_type)

        menu_data = CoffeExplanationSerializer(menu).data
        
        option_data = MenuDetailSerializer(options, many=True).data

        response = {
            "menu_data" : menu_data,
            "options" : option_data
        }

        return Response(response)