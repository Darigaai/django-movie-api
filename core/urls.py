from django.contrib import admin
from django.urls import path, include
from . import yasg
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/', include('movie.urls')),



]
urlpatterns += yasg.urlpatterns


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)