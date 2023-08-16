from django.contrib import admin
from django.urls import path, include
from .views import QuestProvideView,CheckQuestAnswerView,GetQuestView
urlpatterns = [
    path("", GetQuestView.as_view(), name = "quest-get"),
    path("accept/", QuestProvideView.as_view(), name="quest-provide"),
    path("check/",CheckQuestAnswerView.as_view(), name="quest-check")
]