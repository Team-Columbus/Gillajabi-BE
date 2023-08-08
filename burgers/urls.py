from django.contrib import admin
from django.urls import path, include
from .views import MenuListView, DetailMenuListView, SideMenuListView, DrinkListView, CategoryFilterView,PopularMenuView,MoreGoodWithView


urlpatterns = [
    path("list/", MenuListView.as_view(), name="list"),
    path("list/filter/", CategoryFilterView.as_view(), name="list"),
    path("popular/", PopularMenuView.as_view(), name="popular"),
    path("detail/", DetailMenuListView.as_view(), name="setmenu"),
    path("select/sidemenu/", SideMenuListView.as_view(), name="sidemenu"),
    path("select/drink/", DrinkListView.as_view(), name="drink"),
    path("moregood/",MoreGoodWithView.as_view(),name="moregood"),
]
