from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    """
    Is used when getting an object by ID
    """
    class Meta:
        model = Movie
        fields = ('id', 'title', 'desc', 'year')


class MovieMiniSerializer(serializers.HyperlinkedModelSerializer):
    """
    Is used when getting a list of objects
    """
    class Meta:
        model = Movie
        fields = ('id', 'title')
