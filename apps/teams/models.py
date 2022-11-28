from django.db import models

# Create your models here.
class Teams(models.Model):
    name_team = models.CharField(max_length=24, verbose_name='Имя')
    image_team = models.ImageField(upload_to='team_image/', verbose_name=' Фотография')
    work_team = models.CharField(max_length=244, verbose_name='Профессия')

    def __str__(self):
        return self.name_team

    class Meta:
        verbose_name = "Наша команда!"
        verbose_name_plural = "Наша команда!"