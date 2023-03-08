from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
# from users.validators import CorrectUsernameAndNotMe


# class User(AbstractUser, CorrectUsernameAndNotMe):
class User(AbstractUser):
    EMAIL = 'Почта'
    FIRST_NAME = 'Имя'
    LAST_NAME = 'Фамилия'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')
    email = models.EmailField(
        EMAIL,
        unique=True
    )
    first_name = models.CharField(
        verbose_name=FIRST_NAME,
        max_length=settings.MAX_USERNAME_LENGTH
    )
    last_name = models.CharField(
        verbose_name=LAST_NAME,
        max_length=settings.MAX_USERNAME_LENGTH
    )

    class Meta:
        ordering = ('username',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
