# Generated by Django 4.1.3 on 2022-11-28 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='telegram',
            field=models.URLField(default=1, verbose_name='Telegram'),
            preserve_default=False,
        ),
    ]
