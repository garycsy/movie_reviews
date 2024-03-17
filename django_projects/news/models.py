from django.db import models

class News(models.Model):
    headline = models.CharField(max_length=200)
    date = models.DateTimeField()
    body = models.TextField(null=True)


    def __str__(self) -> str:
        return self.headline