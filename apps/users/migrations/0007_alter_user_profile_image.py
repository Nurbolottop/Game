# Generated by Django 4.1.3 on 2022-11-30 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default=1, upload_to='profile_image/', verbose_name='Фотография профиля'),
            preserve_default=False,
        ),
    ]
