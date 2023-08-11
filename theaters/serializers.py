from rest_framework import serializers
from .models import CGVMovie,Detail

class CGVMovie_DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CGVMovie
        fields = ['id', 'movie_poster', 'title', 'theater_floor', 'theater_house']

class MovieTopSerializer(serializers.ModelSerializer):

    class Meta:
        models = Detail
        fields="__all__"

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ["id","seat_number","max_seat","start_time","end_time"]

class CGVMovieSerializer(serializers.ModelSerializer):
    detail = DetailSerializer(many=True, read_only=True)  # Include related Detail data

    class Meta:
        model = CGVMovie
        fields = "__all__"