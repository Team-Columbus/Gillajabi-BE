from django.contrib import admin
from django.urls import path, include
from .views import QuestProvideView
urlpatterns = [
    path("accept/", QuestProvideView.as_view(), name="quest-provide")
]