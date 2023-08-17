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
from traffics.models import Train, Bus
from mysettings import MY_SECRET_KEY
from .serializers import QuestReturnSerializer

# Create your views here.


User = get_user_model()


# class GetQuestView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         try:
#             user_id = request.user

#             user = User.objects.get(user_id=user_id)

#             exist_quest = user_id.quest

#             response = {
#                 "content": exist_quest.content,
#                 "is_accept": exist_quest.is_accept,
#                 "is_do": user.is_quest_do,
#             }
#             return Response(response)
#         except Quest.DoesNotExist:
#             response = {"content": {}, "is_accept": False, "is_do": False}
#             return Response(response)


class QuestAcceptView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user
        exist_quest = user_id.quest

        if exist_quest:
            exist_quest.is_accept = True
            exist_quest.save()

        return Response({"message": "수락완료"})
    
    


class GetQuestView(APIView):
    permission_classes = [IsAuthenticated]

    def generate_quest(self):
        # categories = ["패스트푸드", "영화관", "교통"]
        categories = ["영화관", "교통"]

        choice_category = random.choice(categories)

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
        elif choice_category == "교통":
            transportation_list = ["버스", "기차"]

            choice_transportation = random.choice(transportation_list)

            if choice_transportation == "버스":
                start_terminals = Bus.objects.values_list(
                    "start_terminal", flat=True
                ).distinct()

                choice_start_terminal = random.choice(start_terminals)

                possible_arrive_terminals = Bus.objects.filter(
                    start_terminal=choice_start_terminal
                ).values_list("arrive_terminal", flat=True)

                choice_arrive_terminal = random.choice(possible_arrive_terminals)

                choice_start_time = random.choice(
                    Bus.objects.filter(
                        start_terminal=choice_start_terminal,
                        arrive_terminal=choice_arrive_terminal,
                    ).values_list("start_time", flat=True)
                )

                quest = {
                    "category": choice_category,
                    "transportation": choice_transportation,
                    "start_terminal": choice_start_terminal,
                    "arrive_terminal": choice_arrive_terminal,
                    "start_time": choice_start_time,
                }
                return quest
            else:
                start_station = Train.objects.values_list(
                    "start_station", flat=True
                ).distinct()

                choice_start_station = random.choice(start_station)

                possible_arrive_stations = Train.objects.filter(
                    start_station=choice_start_station
                ).values_list("arrive_station", flat=True)

                choice_arrive_station = random.choice(possible_arrive_stations)

                choice_start_time = random.choice(
                    Train.objects.filter(
                        start_station=choice_start_station,
                        arrive_station=choice_arrive_station,
                    ).values_list("start_time", flat=True)
                )

                quest = {
                    "category": choice_category,
                    "transportation": choice_transportation,
                    "start_terminal": choice_start_station,
                    "arrive_terminal": choice_arrive_station,
                    "start_time": choice_start_time,
                }
                return quest

    def create_and_assign_quest(self, user_id):
        user = User.objects.get(user_id=user_id)
        quest = self.generate_quest()

        # quest_object = Quest.objects.create(content=quest, user=user, is_accept=True)
        quest_object = Quest.objects.create(content=quest, user=user)

        response = {
            "content": quest_object.content,
            "is_accept": quest_object.is_accept,
            "is_do": user.is_quest_do,
        }
        return response

    def get(self, request):
        try:
            user_id = request.user
            exist_quest = user_id.quest

            # if exist_quest:
            #     exist_quest.delete()

            if exist_quest:
                user = User.objects.get(user_id=user_id)
                response = {
                    "content": exist_quest.content,
                    "is_accept": exist_quest.is_accept,
                    "is_do": user.is_quest_do,
                }

            return Response(response)

        except Quest.DoesNotExist:
            user_id = request.user
            response = self.create_and_assign_quest(user_id)

            return Response(response)


class CheckQuestAnswerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user_id = request.user

            answer = request.data["answer"]

            user = User.objects.get(user_id=user_id)

            quest = Quest.objects.get(user_id=user.id)

            if quest.content == answer:
                user.is_quest_do = True
                user.save()
                return Response({"result": True})
            else:
                return Response({"result": False})
        except ExpiredSignatureError:
            return Response({"message": "토큰 만료됨"}, status=status.HTTP_401_UNAUTHORIZED)
