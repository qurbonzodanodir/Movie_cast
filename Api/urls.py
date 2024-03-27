from django.urls import path
from .views import *
urlpatterns = [
    path('create/actor',ActorListApi.as_view()),
    path('create/movie',MovieListApi.as_view()),
    path('create/director',DirectorListApi.as_view()),
    path('create/genres',GenresListApi.as_view()),
    path('create/reviewer',ReviewerListApi.as_view()),
    path('create/rating',ratingListApi.as_view()),
    path('create/movie_genres',movie_genresListApi.as_view()),
    path('create/movie_director',Movie_directorListApi.as_view()),
    path('create/movie-cast',Movie_castListApi.as_view()),
    path('update/actor/<int:pk>',ActorUpdateApi.as_view()),
    path('update/movie/<int:pk>',MovieUpdateApi.as_view()),
    path('update/director/<int:pk>',DirectorUpdateApi.as_view()),
    path('update/genres/<int:pk>',GenresUpdateApi.as_view()),
    path('update/reviewer/<int:pk>',ReviewerUpdateApi.as_view()),
    path('update/rating/<int:pk>',ratingUpdateApi.as_view()),
    path('update/movie_genres/<int:pk>',movie_genresUpdateApi.as_view()),
    path('update/movie_director/<int:pk>',Movie_directorUpdateApi.as_view()),
    path('update/movie_cast/<int:pk>',Movie_castUpdateApi.as_view()),


]
