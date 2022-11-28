from django.db import models

# Create your models here.
class Contact(models.Model):
    phone = models.CharField(max_length=244, verbose_name='Телефонный номер: ')
    email = models.EmailField(max_length=244, verbose_name='Почта')
    address = models.CharField(max_length=244, verbose_name='Адрес')
    facebook = models.URLField(verbose_name='Faceebook')
    instagram = models.URLField(verbose_name='Instagram')
    youtube = models.URLField(verbose_name='Youtube')
    telegram = models.URLField(verbose_name='Telegram')

    
    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = "Контакты"
        verbose_name_plural = "Контакты"

class Contact_detail(models.Model):
    name =models.CharField(max_length =255)
    subject = models.CharField(max_length=244)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return f"{self.name} {self.message}"

    class Meta:
        verbose_name_plural = "Заявки"
        verbose_name = "Заявки"  