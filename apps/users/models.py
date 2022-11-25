from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to=244,
        verbose_name='Фотография профиля',
        blank=True,null =True
    )

    phone = models.CharField(
        max_length=255, 
        verbose_name='Телефонный номер',
        blank=True, null=True
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
        
