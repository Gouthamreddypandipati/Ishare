# Generated by Django 3.1.5 on 2021-04-09 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_remove_agcomment_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agcomment',
            name='text',
            field=models.TextField(blank='True', null='True'),
        ),
    ]
