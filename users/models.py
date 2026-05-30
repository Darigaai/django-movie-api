from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# 1. Создали кастомного пользователя User
# 2. Настроили вход по email вместо username
# 3. Подключили JWT через SimpleJWT
# 4. Сделали регистрацию, которая сразу возвращает access и refresh token
# 5. Сделали login и refresh endpoints
# 6. Настроили Swagger / Redoc документацию







class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username']

    def __str__(self) -> str:
        return self.email
    










