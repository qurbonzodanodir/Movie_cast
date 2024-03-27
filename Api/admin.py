from django.contrib import admin
from .models import *

admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Genres)
admin.site.register(Reviewer)
admin.site.register(movie_genres)
admin.site.register(Movie_cast)
admin.site.register(Movie_director)
admin.site.register(rating)
