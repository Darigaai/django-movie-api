from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GenreSerializer, ActorSerializer, MovieSerializer
from .models import Genre, Actor, Movie
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import permissions

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [permissions.IsAuthenticated]


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = [permissions.IsAuthenticated]



class MovieViewSet(viewsets.ModelViewSet):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = {
        'year': ['gte', 'lte', 'exact'], 
        'budget': ['gte', 'lte', 'exact']
    }

    search_fields = ['title', 'actors__name', 'genres__title']
    ordering_fields = ['year', 'budget']

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
         serializer.save(user=self.request.user)





       