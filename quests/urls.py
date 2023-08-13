from django.contrib import admin
from django.urls import path, include
from .views import QuestProvideView,CheckQuestAnswerView
urlpatterns = [
    path("accept/", QuestProvideView.as_view(), name="quest-provide"),
    path("check/",CheckQuestAnswerView.as_view(), name="quest-check")
]