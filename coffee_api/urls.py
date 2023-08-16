from django.urls import path
from .views import CoffeeMenuListCreateView, DetailOptionView
from .views import DetailSerializerListCreateView

urlpatterns = [
    path('menu/', CoffeeMenuListCreateView.as_view(), name='coffee-menu-list-create'),
    path('deteil/', DetailSerializerListCreateView.as_view(), name='coffee-detail-page'),
    path('option/', DetailOptionView.as_view(), name="options")
]
