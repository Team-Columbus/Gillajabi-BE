from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import McdonalSerializer,SetMenuSerializer
from .models import Mcdonald
# Create your views here.


class MenuListView(APIView):
    
    def post(self,request):
        
        menu_category = request.data["menu_category"]
        data = Mcdonald.objects.filter(menu_category = menu_category)
        serilaizer = McdonalSerializer(data, many=True)
        return Response(serilaizer.data)    
        

class SetMenuListView(APIView):
    
    def post(self, request):
        
        menu_name = request.data["menu_name"]
        menu = Mcdonald.objects.get(menu_name = menu_name)
        
        serilaized_pets = SetMenuSerializer(menu.set_menus.all(),many=True).data
        
        return Response(serilaized_pets)
        
        
        