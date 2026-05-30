from django.urls import path, include
from rest_framework import routers
from .views import GenreViewSet, ActorViewSet, MovieViewSet
router = routers.DefaultRouter()

router.register(r'genres', GenreViewSet)
router.register(r'actors', ActorViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = router.urls