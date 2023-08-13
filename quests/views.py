import random, jwt
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from jwt.exceptions import ExpiredSignatureError
from theaters.models import CGVMovie, Detail
from django.contrib.auth import get_user_model
from quests.models import Quest
from burgers.models import Mcdonald, DetailMenu
from mysettings import MY_SECRET_KEY
from .serializers import QuestReturnSerializer

# Create your views here.


User = get_user_model()


class QuestProvideView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user_id = request.user

            user = User.objects.get(user_id=user_id)
            quest = generate_quest()

            quest_object = Quest.objects.create(
                content=quest, user=user, is_accept=True
            )

            response = QuestReturnSerializer(quest_object).data
            return Response(response)

        except ExpiredSignatureError:
            return Response({"message": "토큰 만료됨"}, status=status.HTTP_401_UNAUTHORIZED)


class CheckQuestAnswerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user_id = request.user

            answer = request.data["answer"]

            user = User.objects.get(user_id=user_id)

            quest = Quest.objects.get(user_id=user.id)

            if quest.content == answer:
                return Response({"result": True})
            else:
                return Response({"result": False})
        except ExpiredSignatureError:
            return Response({"message": "토큰 만료됨"}, status=status.HTTP_401_UNAUTHORIZED)


def generate_quest():
    # categories = ["패스트푸드","영화관","교통"]

    # choice_category = random.choice(categories)
    choice_category = "패스트푸드"
    # choice_category = "영화관"

    if choice_category == "패스트푸드":
        menu_options = ["단품", "세트"]

        choice_menu_option = random.choice(menu_options)

        other_options = ["음료", "사이드", "선택안함"]

        choice_other_option = random.choice(other_options)

        if choice_menu_option == "단품":
            burger_list = Mcdonald.objects.filter(menu_category="버거")
        else:
            burger_list = DetailMenu.objects.filter(menu_category="버거")

        burger_name_list = [burger.menu_name for burger in burger_list]

        choice_burger = random.choice(burger_name_list)

        burger_count = random.randint(1, 2)

        choice_side_menu = None
        side_menu_count = 0

        if choice_other_option != "선택안함":
            side_menus = Mcdonald.objects.filter(menu_category=choice_other_option)

            side_name_list = [side.menu_name for side in side_menus]

            choice_side_menu = random.choice(side_name_list)

            side_menu_count = random.randint(1, 2)

        quest = {
            "category": choice_category,
            "burger": {"name": choice_burger, "count": burger_count},
            "side": {"name": choice_side_menu, "count": side_menu_count},
        }

        return quest

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
        quest = {
            "category": choice_category,
            "title": choice_movie,
            "time": choice_time,
            "ticket": target,
        }

        return quest
    elif choice_category == "고통":
        pass
