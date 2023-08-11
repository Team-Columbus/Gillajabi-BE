import random
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from theaters.models import CGVMovie
# Create your views here.


User = get_user_model()



class QuestProvideView(APIView):

    def post(Self,request):

        user_id = request.data["user_id"]

        user = User.objects.get(user_id=user_id)

    


def generate_quest():

    categories = ["패스트푸드","영화관","교통"]

    choice_category = random.choice(categories)

    if choice_category == "패스트푸드":
        pass
    elif choice_category == "영화관":
        movies = CGVMovie.objects.all()

        moive_list = [movie.name for movie in movies]

        choice_movie = random.choices(moive_list)

        



    elif choice_category =="교통":
        pass
    
    

