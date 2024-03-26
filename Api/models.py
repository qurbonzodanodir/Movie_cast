from django.db import models

class Actor(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    act_fname = models.CharField(max_length = 70)
    act_lname = models.CharField(max_length = 100)
    act_gender = models.CharField(max_length = 2, choices = GENDER_CHOICES)



class Movie(models.Model):
    Language_CHOICES = (
        ('Ru', 'Russian'),
        ('En', 'English'),
        ('TJ', 'Tajik'),
    )
    mov_title = models.CharField(max_length = 100)
    mov_year = models.DateField()
    mov_time = models.DateTimeField()
    mov_lang = models.CharField(max_length = 2,choices = Language_CHOICES)
    mov_dt_rel = models.DateField()
    mov_country = models.CharField(max_length = 100)   

class Director(models.Model):
    dir_fname = models.CharField(max_length = 70)
    dir_lname = models.CharField(max_length = 100)


class Genres(models.Model):
    gen_tittle = models.CharField(max_length = 100)

class Reviewer(models.Model):
    rev_name = models.CharField(max_length = 100)    



class Movie_cast(models.Model):
    act_id = models.ForeignKey(Actor,on_delete = models.CASCADE)
    movie_id = models.ForeignKey(Movie,on_delete = models.CASCADE)



class Movie_director(models.Model):
    movie_id = models.ForeignKey(Movie,on_delete = models.CASCADE)
    dir_id = models.ForeignKey(Director,on_delete = models.CASCADE)


class movie_genres(models.Model):
    movie_id = models.ForeignKey(Movie,on_delete = models.CASCADE)
    genres_id = models.ForeignKey(Genres,on_delete = models.CASCADE)



class rating(models.Model):
    movie_id = models.ForeignKey(Movie,on_delete = models.CASCADE)
    reviewer = models.ForeignKey(Reviewer,on_delete = models.CASCADE)
    rev_starts = models.IntegerField()
    num_o_ratings = models.IntegerField()





