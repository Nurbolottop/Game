# Generated by Django 4.1.3 on 2022-11-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.CharField(max_length=244, verbose_name='Достижение про игру')),
                ('desc_game', models.TextField(verbose_name='Описание')),
                ('bonuse', models.CharField(max_length=255, verbose_name='Достижение про бонусы')),
                ('desc_bonus', models.TextField(verbose_name='Описание')),
                ('help', models.CharField(max_length=255, verbose_name='Достижение про поддержку')),
                ('desc_help', models.TextField(verbose_name='Описание')),
            ],
        ),
    ]
