# Generated by Django 4.1.3 on 2022-11-25 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('live', models.CharField(max_length=244, verbose_name='Количество Прямых эфиров')),
                ('players', models.CharField(max_length=244, verbose_name='Количество Игроков')),
                ('money', models.CharField(max_length=255, verbose_name='Ежедневная награда')),
            ],
            options={
                'verbose_name': 'Данные',
                'verbose_name_plural': 'Данные',
            },
        ),
    ]