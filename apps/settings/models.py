from django.db import models

# Create your models here.
class Setting(models.Model):
    name = models.CharField(
        max_length= 255, 
        verbose_name='Название сайта'
    )
    desc = models.TextField(
        verbose_name='Описание сайта'
        )
    logo = models.ImageField(
        upload_to='logo_site/', 
        verbose_name='Логотип сайта '
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Настройки"
        verbose_name_plural = 'Настройка'

class Data(models.Model):
    live = models.CharField(max_length=244, verbose_name='Количество Прямых эфиров')
    players = models.CharField(max_length=244,verbose_name='Количество Игроков')
    money = models.CharField(max_length=255, verbose_name='Ежедневная награда')
    
    def __str__(self):
        return self.live

    class Meta:
        verbose_name = "Данные"
        verbose_name_plural = 'Данные'

class Achievement(models.Model):
    game = models.CharField(max_length=244,verbose_name='Достижение про игру')
    desc_game = models.TextField(verbose_name='Описание')

    bonuse = models.CharField(max_length=255, verbose_name='Достижение про бонусы')
    desc_bonus = models.TextField(verbose_name='Описание')

    help = models.CharField(max_length=255, verbose_name='Достижение про поддержку')
    desc_help = models.TextField(verbose_name='Описание')


class Game(models.Model):
    name_game = models.CharField(max_length=244,verbose_name='Название игры')
    desc_game = models.TextField(max_length=255,verbose_name='Описание игры')
    url_game = models.URLField(verbose_name='Ссылка на игру')
    image_game = models.ImageField(upload_to='GamePhto/', verbose_name="Фотография игры ")

    def __str__(self):
        return self.name_game

    class Meta:
        verbose_name = "Игры"
        verbose_name_plural = 'Игры'
