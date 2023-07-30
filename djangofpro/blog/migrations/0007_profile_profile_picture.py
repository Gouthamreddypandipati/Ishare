# Generated by Django 3.1.5 on 2021-02-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank='True', default='images/default.jpg', null='True', upload_to='images/profile_picture/'),
            preserve_default='True',
        ),
    ]
