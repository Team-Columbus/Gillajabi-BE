import random, jwt
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from theaters.models import CGVMovie, Detail
from quests.models import Quest
from mysettings import MY_SECRET_KEY

# Create your views here.


User = get_user_model()


class QuestProvideView(APIView):
    def post(self, request):
        access_token = request.data["access_token"]
        decoded = jwt.decode(access_token, MY_SECRET_KEY, algorithms=["HS256"])
        user_id = decoded.get("user_id")

        user = User.objects.get(id=user_id)

        quest = generate_quest()
        Quest.objects.create(content=quest, user=user)

        return Response(quest)


def generate_quest():
    # categories = ["패스트푸드","영화관","교통"]

    # choice_category = random.choice(categories)
    choice_category = "영화관"

    if choice_category == "패스트푸드":
        pass
    elif choice_category == "영화관":
        movies = CGVMovie.objects.all()

        movie_list = [movie.title for movie in movies]

        choice_movie = random.choices(movie_list)[0]

        data = CGVMovie.objects.get(title=choice_movie)

        details = Detail.objects.filter(movie=data)

        time_list = [detail.start_time for detail in details]

        choice_time = random.choices(time_list)[0]

        target = {
            "normal": random.randint(1, 2),
            "teen": random.randint(0, 2),
            "disabled": random.randint(0, 2),
            "silver": random.randint(0, 2),
        }
        return {
            "category": choice_category,
            "title": choice_movie,
            "time": choice_time,
            "ticket": target,
        }
    elif choice_category == "고통":
        pass
