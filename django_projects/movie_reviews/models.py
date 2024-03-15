from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='/movie_reviews/images/')
    url = models.URLField(blank=True)