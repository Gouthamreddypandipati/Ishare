# Generated by Django 3.1.5 on 2021-03-14 06:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0020_hpost_dislikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='agpost',
            name='dislikes',
            field=models.ManyToManyField(blank='True', related_name='blog_postaglik', to=settings.AUTH_USER_MODEL),
        ),
    ]