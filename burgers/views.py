import random
from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import (
    McdonaldSerializer,
    DetailMenuReturnSerializer,
    DrinkSelectSerializer,
    SingleMenuReturnSerializer,
    MediumSideMenuReturnSerializer,
    LargeSideMenuReturnSerializer,
    PopularMenuReturnSerilaizer,
    MoreGoodSerializer,
)
from .models import Mcdonald,DetailMenu

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


class DetailMenuListView(APIView):
    def post(self, request):
        menu_name = request.data["menu_name"]

        menu = Mcdonald.objects.get(menu_name=menu_name)
        
        serialized_single = SingleMenuReturnSerializer(menu).data

        serilaized_detail = DetailMenuReturnSerializer(menu.detail_menus.all(), many=True).data

        return Response(
                {"single_menus": serialized_single, "detail_menus": serilaized_detail})



class SideMenuListView(APIView):
    def post(self, request):

        menu_size = request.data["menu_size"]
        menu_name = "감자 튀김"


        potato = DetailMenu.objects.get(menu_name__contains=menu_name, menu_size = menu_size)
        others = Mcdonald.objects.exclude(Q(menu_name=menu_name) | ~Q(menu_category="사이드"))


        serialized_potato = DetailMenuReturnSerializer(potato).data
        if menu_size == "미디엄":
            serialized_others = MediumSideMenuReturnSerializer(others, many=True).data
        elif menu_size == "라지":
            serialized_others = LargeSideMenuReturnSerializer(others, many=True).data

        response = {
                "poptato" : serialized_potato,
                "others" : serialized_others
            }
        return Response(response)


class DrinkListView(APIView):
    def post(self, request):

        menu_size = request.data["menu_size"]

        drinks = DetailMenu.objects.filter(menu_size = menu_size, menu_category = "음료")

        serialized_data = DrinkSelectSerializer(drinks, many=True).data

        return Response(serialized_data)
        
class CategoryFilterView(APIView):
    def post(self, request):
        food_category = request.data["food_category"]

        data = Mcdonald.objects.filter(food_category=food_category)

        serialized_data = McdonaldSerializer(data, many=True).data

        return Response(serialized_data)

class PopularMenuView(APIView):
    
    def get(self,request):

        data = Mcdonald.objects.filter(
            Q(menu_name="불고기 버거") | Q(menu_name="통새우 버거") | Q(menu_name="할라피뇨 치킨 버거")
        )

        serialized_data = PopularMenuReturnSerilaizer(data, many=True).data

        return Response(serialized_data)
    
class MoreGoodWithView(APIView):

    def post(self,request):
        
        menu_list = request.data["menu_list"]

        other_menus = Mcdonald.objects.filter(Q(menu_category="버거") | Q(menu_category="사이드")).exclude(menu_name__in=menu_list)


        random_others = random.sample(list(other_menus), min(3, len(other_menus)))

        serialized_data = MoreGoodSerializer(random_others,many=True).data

        return Response(serialized_data)
    





    
