from django.urls import path
from . import views

urlpatterns = [
    path('CGVmovies_top/', views.get_top_movies, name='movie_top'),
    path('CGVmovie_list/', views.get_movie_list, name='movie_list'),
    path('CGVmovie_detail/<int:pk>/', views.get_movie_detail, name='movie_detail'),
]