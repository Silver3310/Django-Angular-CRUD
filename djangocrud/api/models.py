from django.db import models


class Movie(models.Model):
    """
    Custom model for movies
    """
    title = models.CharField(max_length=32)
    desc = models.TextField(max_length=256)
    year = models.IntegerField()

    def __str__(self):
        return f'{self.title} ({self.year})'
