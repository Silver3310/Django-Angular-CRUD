from rest_framework import viewsets
from .serializers import MovieSerializer, MovieMiniSerializer
from .models import Movie
from rest_framework.response import Response


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows movies to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request, *args, **kwargs):
        """
        A method for GET requests when returning all elements,
        returns only ids and titles of movies
        """
        # to update values
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(
            movies,
            many=True
        )
        return Response(serializer.data)
