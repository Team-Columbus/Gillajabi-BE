from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import random
from .models import CGVMovie, Detail
from .serializers import CGVMovieSerializer


@api_view(["GET"])
def get_top_movies(request):
    movies = CGVMovie.objects.all()
    random_movies = random.sample(list(movies), 3)
    top_movies_with_first_time = []

    for movie in random_movies:
        if movie.detail.exists():
            title = movie.title
            rating = movie.rating
            poster = movie.movie_poster
            seat_number = movie.detail.first().seat_number
            max_seat = movie.detail.first().max_seat
            start_time = movie.detail.first().start_time
            end_time = movie.detail.first().end_time

        movie_data = {
            "title": title,
            "rating": rating,
            "poster": poster,
            "seat_number": seat_number,
            "max_seat": max_seat,
            "start_time": start_time,
            "end_time": end_time,
        }
        top_movies_with_first_time.append(movie_data)

    return Response(top_movies_with_first_time, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_movie_list(request):
    movies = CGVMovie.objects.all()
    serializer = CGVMovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_movie_detail(request, pk):
    try:
        detail = Detail.objects.get(id=pk)
        movie = detail.movie

        movie_data = {
            "id": movie.id,
            "movie_poster": movie.movie_poster,
            "title": movie.title,
            "rating": movie.rating,
            "theater_house": movie.theater_house,
            "theater_floor": movie.theater_floor,
            "seat_number": detail.seat_number,
            "max_seat": detail.max_seat,
            "start_time": detail.start_time,
            "end_time": detail.end_time,
        }
    except Detail.DoesNotExist:
        return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)

    return Response(movie_data)
