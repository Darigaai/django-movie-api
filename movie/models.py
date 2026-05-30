from django.db import models
# 7. Создали модели фильмов, жанров, актёров
# 8. Сделали serializers для API
# 9. Сделали ViewSet-ы для CRUD
# 10. Подключили router, чтобы автоматически получить endpoints
# 11. Добавили скрипт populate_db.py для заполнения базы фильмами
from users.models import User

class Genre(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    def __str__(self) -> str:
        return self.title
    
class Actor(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name='g_movies')
    actors = models.ManyToManyField(Actor, related_name='actors')
    title = models.CharField(max_length=255)
    description = models.TextField()
    poster = models.ImageField(upload_to='movies/', blank=True, null=True)
    year = models.PositiveIntegerField()
    country = models.CharField(max_length=255)
    directors = models.ManyToManyField(Actor, related_name='directors')
    world_premiere = models.DateField()
    budget = models.PositiveIntegerField()
    fees_in_usa = models.PositiveIntegerField()
    fees_in_world = models.PositiveIntegerField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
    
    