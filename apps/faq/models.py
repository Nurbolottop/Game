from django.db import models

# Create your models here.
class Faq(models.Model):
    name = models.CharField(max_length=244, verbose_name='Вопрос!')
    desc = models.TextField(verbose_name='Ответ!')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Часто задаваемые вопросы!"
        verbose_name_plural = "Часто задаваемые вопросы!"