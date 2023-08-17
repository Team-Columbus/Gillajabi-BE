from django.contrib import admin
from django.urls import path, include
from .views import GetQuestView, CheckQuestAnswerView, GetQuestView, QuestAcceptView

urlpatterns = [
    path("", GetQuestView.as_view(), name="quest-bring"),
    path("accept/", QuestAcceptView.as_view(), name="quest-accept"),
    path("check/", CheckQuestAnswerView.as_view(), name="quest-check"),
]
