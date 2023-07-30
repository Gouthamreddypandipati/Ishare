from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class UsModel(models.Model):
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	currentstatus=models.CharField(max_length=255,null='True',blank='True')
	profile_pick=models.ImageField(default="images/default.jpg",null='True',blank='True',upload_to="images/profile/")
	dateofbirth=models.TextField(null='True',blank='True')
	facebook_id=models.TextField(null='True',blank='True')
	instagram_id=models.TextField(null='True',blank='True')
	whatsapp_number=models.DecimalField(max_digits=10,decimal_places=0,null='True',blank='True')
	twitter_id=models.TextField(null='True',blank='True')
	youtubechannel_name=models.TextField(null='True',blank='True')
	linked_in_profile=models.TextField(null='True',blank='True')
	yourquote=models.TextField(null='True',blank='True')

	def __str__(self):
		return str(self.yourquote)
	def get_absolute_url(self):
		return reverse('main')