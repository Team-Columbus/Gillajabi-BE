from rest_framework import serializers
from .models import CGVMovie

# CGVMovie 모델에 대한 Serializer
class CGVMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CGVMovie
        fields = ['id', 'movie_poster','title', 'rating', 'seat_number', 'max_seat']

class CGVMovie_DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CGVMovie
        fields = ['id', 'movie_poster', 'title', 'theater_floor', 'theater_house']