from django.db import models

# Create your models here.
class News(models.Model):
    name_news = models.CharField(max_length=255, verbose_name='Название сайта.')
    image_news = models.ImageField(upload_to="news_image/", verbose_name='Фотография нововсти.')
    description_news = models.TextField(verbose_name='Описание новости.')
    created_news = models.DateField(auto_now_add = True)
