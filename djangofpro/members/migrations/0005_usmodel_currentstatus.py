# Generated by Django 3.1.5 on 2021-02-26 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20210226_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='usmodel',
            name='currentstatus',
            field=models.CharField(blank='True', max_length=255, null='True'),
            preserve_default='True',
        ),
    ]