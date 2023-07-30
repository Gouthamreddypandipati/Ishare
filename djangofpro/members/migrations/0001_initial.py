# Generated by Django 3.1.5 on 2021-01-28 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pick', models.ImageField(blank='True', null='True', upload_to='images/profile/')),
                ('dateofbirth', models.DateField(blank='True', null='True')),
                ('facebook_id', models.TextField(blank='True', null='True')),
                ('instagram_id', models.TextField(blank='True', null='True')),
                ('whatsapp_number', models.DecimalField(decimal_places=0, max_digits=10)),
                ('twitter_id', models.TextField(blank='True', null='True')),
                ('youtubechannel_name', models.TextField(blank='True', null='True')),
                ('linked_in_profile', models.TextField(blank='True', null='True')),
                ('yourquote', models.TextField(blank='True', null='True')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
