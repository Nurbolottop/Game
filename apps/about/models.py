from django.db import models

# Create your models here.
class About(models.Model):
    name_about_1= models.CharField(max_length=123, verbose_name="Выгоды - 1")
    name_desc_1 =models.TextField(verbose_name='Описание про <<Выгоды - 1>>')

    name_about_2= models.CharField(max_length=223, verbose_name="Выгоды - 2")
    name_desc_2 =models.TextField(verbose_name='Описание про <<Выгоды - 2>>')
    
    name_about_3= models.CharField(max_length=333, verbose_name="Выгоды - 3")
    name_desc_3 =models.TextField(verbose_name='Описание про <<Выгоды - 3>>')

    def __str__(self):
        return self.name_about_1

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"