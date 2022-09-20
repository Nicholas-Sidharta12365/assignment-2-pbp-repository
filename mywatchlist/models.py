from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class Watchlist(models.Model):
    watched = models.BooleanField()
    title = models.TextField()
    # rating = models.FloatField(
    #     default=1.0,
    #     validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]

    # )
    release_date = models.TextField()
    review = models.TextField()