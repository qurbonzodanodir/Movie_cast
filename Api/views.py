from rest_framework import generics
from rest_framework.response import responses
from .serializer import *
from rest_framework import permissions
from .models import *


class ActorListApi(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MovieListApi(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

class DirectorListApi(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GenresListApi(generics.ListCreateAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)  


class ReviewerListApi(generics.ListCreateAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ratingListApi(generics.ListCreateAPIView):
    queryset = rating.objects.all()
    serializer_class = ratingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
class movie_genresListApi(generics.ListCreateAPIView):
    queryset = movie_genres.objects.all()
    serializer_class = movie_genresSerializer 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Movie_castListApi(generics.ListCreateAPIView):
    queryset = Movie_cast.objects.all()
    serializer_class = Movie_castSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Movie_directorListApi(generics.ListCreateAPIView):
    queryset = Movie_director.objects.all()
    serializer_class = movie_genresSerializer 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)







class ActorUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class MovieUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

class DirectorUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class GenresUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer  
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ReviewerUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ratingUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = rating.objects.all()
    serializer_class = rating
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    
class movie_genresUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = movie_genres.objects.all()
    serializer_class = rating 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Movie_castUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie_cast.objects.all()
    serializer_class = rating
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class Movie_directorUpdateApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie_director.objects.all()
    serializer_class = rating 
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


