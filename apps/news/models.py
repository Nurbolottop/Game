from django.db import models

from apps.users.models import User
# Create your models here.
class News(models.Model):
    name_news = models.CharField(max_length=255, verbose_name='Название сайта.')
    image_news = models.ImageField(upload_to="news_image/", verbose_name='Фотография нововсти.')
    description_news = models.TextField(verbose_name='Описание новости.')
    created_news = models.DateField(auto_now_add = True)
    

    def __str__(self):
        return self.name_news

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    post = models.ForeignKey(News, on_delete=models.CASCADE, related_name="post_comment")
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text}"

    class Meta:
        ordering = ("-created",)