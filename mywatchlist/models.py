from django.db import models
# Create your models here.

class Watchlist(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.TextField()
    release_date = models.TextField()
    review = models.TextField()