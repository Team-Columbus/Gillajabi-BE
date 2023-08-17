from django.urls import path
from . import views

urlpatterns = [
    #기차 urls
    path('start_train_list/', views.get_start_train_list, name='start_train_list'),
    path('arrive_train_list/', views.get_arrive_train_list, name='arrive_train_list'),
#    path('search_start_station/', views.SearchStartStation.as_view(), name='search_start_train'),
#    path('search_arrive_station/', views.SearchArriveStation.as_view(), name='search_arrive_station'),
    path('train_ticket/', views.get_train_ticket, name='train_ticket'),

    # 버스 urls
#    path('start_bus_list/', views.get_start_bus_list, name='start_bus_list'),
    path('arrive_bus_list/', views.get_arrive_bus_list, name='arrive_bus_list'),
#    path('search_arrive_bus/', views.SearchArriveTerminal.as_view(), name='search_arrive_bus'),    
    path('bus_ticket/', views.get_terminal_ticket, name='bus_ticket'),
]