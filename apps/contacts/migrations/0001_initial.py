# Generated by Django 4.1.3 on 2022-11-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=244, verbose_name='Телефонный номер: ')),
                ('email', models.EmailField(max_length=244, verbose_name='Почта')),
                ('address', models.CharField(max_length=244, verbose_name='Адрес')),
                ('facebook', models.URLField(verbose_name='Faceebook')),
                ('instagram', models.URLField(verbose_name='Instagram')),
                ('youtube', models.URLField(verbose_name='Youtube')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]
