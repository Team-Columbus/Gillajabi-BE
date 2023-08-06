from django.contrib import admin
from django.urls import path, include
from .views import MenuListView, SetMenuListView, SideMenuListView, DrinkListView, CategoryFilterView


urlpatterns = [
    path("list/", MenuListView.as_view(), name="list"),
    path("list/filter/", CategoryFilterView.as_view(), name="list"),
    # path("list/popular/")
    path("setmenu/", SetMenuListView.as_view(), name="setmenu"),
    path("select/sidemenu/", SideMenuListView.as_view(), name="sidemenu"),
    path("select/drink/", DrinkListView.as_view(), name="drink"),
]
