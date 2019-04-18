from rest_framework import viewsets
from .serializers import MovieSerializer, MovieMiniSerializer
from .models import Movie
from rest_framework.response import Response
from .tasks import added, removed, changed


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

    def create(self, request, *args, **kwargs):
        """
        A method for POST requests, inform about adding
        """
        added.delay(request.data['title'])
        return super(MovieViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        A method for PUT requests, inform about updating
        """
        changed.delay(request.data['title'])
        return super(MovieViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        A method for delete requests, inform about deleting
        """
        id_to_delete = request.parser_context['kwargs']['pk']
        removed.delay(Movie.objects.get(id=id_to_delete).title)
        return super(MovieViewSet, self).destroy(request, *args, **kwargs)
