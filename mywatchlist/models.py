from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Watchlist(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    rating = models.FloatField(
        validators=[
            MaxValueValidator(5.0), MinValueValidator(1.0)
            ]
        )
    release_date = models.TextField()
    review = models.TextField()