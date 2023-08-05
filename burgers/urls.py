from django.contrib import admin
from django.urls import path, include
from .views import MenuListView, SetMenuListView


urlpatterns = [
    path("list/", MenuListView.as_view(), name="list"),
    path("setmenu/", SetMenuListView.as_view(), name="setmenu"),
]
