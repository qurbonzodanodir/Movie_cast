from rest_framework import serializers
from .models import *


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__' 


class  DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'  


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'

class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = '__all__' 

class Movie_castSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_cast
        fields = '__all__'  

class Movie_directorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_director
        fields = '__all__'

class ratingSerializer(serializers.ModelSerializer):
    class Meta:
        model = rating
        fields = '__all__'


class movie_genresSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie_genres
        fields = '__all__'
        

                    