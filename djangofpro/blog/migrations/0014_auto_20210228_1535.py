# Generated by Django 3.1.5 on 2021-02-28 10:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_delete_useprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='expost',
            name='dislikes',
            field=models.ManyToManyField(blank='True', related_name='blog_postexlik', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expost',
            name='likes',
            field=models.ManyToManyField(blank='True', related_name='blog_postexdis', to=settings.AUTH_USER_MODEL),
        ),
    ]
