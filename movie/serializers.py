from rest_framework import serializers
from .models import Genre, Actor, Movie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    directors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )
    actors = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Actor.objects.all()
    )
    genres = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Genre.objects.all()
    )

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ['user']


    