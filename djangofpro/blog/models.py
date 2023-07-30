from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from django.db.models.signals import post_save
from django.dispatch import receiver
class ExPost(models.Model):
	title=models.CharField(max_length=255)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	text=models.TextField()
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	likes=models.ManyToManyField(User,related_name='blog_postexdis',blank="True")
	header_image=models.ImageField(null='True',blank='True',upload_to="images/Exercises/")
	dislikes=models.ManyToManyField(User,related_name='blog_postexlik',blank="True")
	

	#class Meta:
		#ordering=['-date']
	def total_likes(self):
		return self.likes.count()
	def total_dislikes(self):
		return self.dislikes.count()
	def __str__(self):
		return str(self.title)	
	def get_absolute_url(self):
		return reverse('main')

class EdPost(models.Model):
	title=models.CharField(max_length=255)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	text=models.TextField()
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	dislikes=models.ManyToManyField(User,related_name='blog_postedlik',blank="True")
	likes=models.ManyToManyField(User,related_name='blog_posted',blank="True")
	header_image=models.ImageField(null='True',blank='True',upload_to="images/Education/")
	#class Meta:
		#ordering=['-date']
	def total_likes(self):
		return self.likes.count()
	def total_dislikes(self):
		return self.dislikes.count()
	def __str__(self):
		return str(self.title)
	def get_absolute_url(self):
		return reverse('main')


class SPost(models.Model):
	title=models.CharField(max_length=255)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	text=models.TextField()
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	likes=models.ManyToManyField(User,related_name='blog_postsp',blank="True")
	dislikes=models.ManyToManyField(User,related_name='blog_postsplik',blank="True")
	header_image=models.ImageField(null='True',blank='True',upload_to="images/Sports/")
	#class Meta:
		#ordering=['-date']
	def total_likes(self):
		return self.likes.count()
	def total_dislikes(self):
		return self.dislikes.count()
	def __str__(self):
		return str(self.title)
	def get_absolute_url(self):
		return reverse('main')

class TPost(models.Model):
	title=models.CharField(max_length=255)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	text=models.TextField()
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	likes=models.ManyToManyField(User,related_name='blog_postto',blank="True")
	dislikes=models.ManyToManyField(User,related_name='blog_posttolik',blank="True")
	header_image=models.ImageField(null='True',blank='True',upload_to="images/Tourism/")
	#class Meta:
	#	ordering=['-date']
	def total_likes(self):
		return self.likes.count()
	def total_dislikes(self):
		return self.dislikes.count()
	def __str__(self):
		return str(self.title)
	def get_absolute_url(self):
		return reverse('main')

class HPost(models.Model):
	title=models.CharField(max_length=255)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	text=models.TextField()
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	likes=models.ManyToManyField(User,related_name='blog_posthe',blank="True")
	dislikes=models.ManyToManyField(User,related_name='blog_posthelik',blank="True")
	header_image=models.ImageField(null='True',blank='True',upload_to="images/Health/")
	#class Meta:
	#	ordering=['-date']
	def total_likes(self):
		return self.likes.count()
	def total_dislikes(self):
		return self.dislikes.count()
	def __str__(self):
		return str(self.title)
	def get_absolute_url(self):
		return reverse('main')

class DPost(models.Model):
	title=models.CharField(max_length=255)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	text=models.TextField()
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	likes=models.ManyToManyField(User,related_name='blog_postde',blank="True")
	dislikes=models.ManyToManyField(User,related_name='blog_postdelik',blank="True")
	header_image=models.ImageField(null='True',blank='True',upload_to="images/Devotinal/")
	#class Meta:
	#	ordering=['-date']
	def total_likes(self):
		return self.likes.count()
	def total_dislikes(self):
		return self.dislikes.count()
	def __str__(self):
		return str(self.title)
	def get_absolute_url(self):
		return reverse('main')

class OPost(models.Model):
	title=models.CharField(max_length=255)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	text=models.TextField()
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	likes=models.ManyToManyField(User,related_name='blog_postot',blank="True")
	dislikes=models.ManyToManyField(User,related_name='blog_postotlik',blank="True")
	header_image=models.ImageField(null='True',blank='True',upload_to="images/Others/")
	#class Meta:
	#	ordering=['-date']
	def total_likes(self):
		return self.likes.count()
	def total_dislikes(self):
		return self.dislikes.count()
	def __str__(self):
		return str(self.title)
	def get_absolute_url(self):
		return reverse('main')



class EnPost(models.Model):
	title=models.CharField(max_length=255)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	text=models.TextField()
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	likes=models.ManyToManyField(User,related_name='blog_posten',blank="True")
	dislikes=models.ManyToManyField(User,related_name='blog_posentlik',blank="True")
	header_image=models.ImageField(null='True',blank='True',upload_to="images/Entertainment/")
	#class Meta:
		#ordering=['-date']
	def total_likes(self):
		return self.likes.count()
	def total_dislikes(self):
		return self.dislikes.count()
	def __str__(self):
		return str(self.title)
	def get_absolute_url(self):
		return reverse('main')
class AgPost(models.Model):
	title=models.CharField(max_length=255)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	text=models.TextField()
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	likes=models.ManyToManyField(User,related_name='blog_postag',blank="True")
	dislikes=models.ManyToManyField(User,related_name='blog_postaglik',blank="True")
	header_image=models.ImageField(null='True',blank='True',upload_to="images/Agriculture/")
	#class Meta:
	#	ordering=['-id']
	def total_likes(self):
		return self.likes.count()
	def total_dislikes(self):
		return self.dislikes.count()
	def __str__(self):
		return str(self.title)
	def get_absolute_url(self):
		return reverse('main')
class ExVideo(models.Model):
	caption=models.CharField(max_length=100)
	video=models.FileField(null='True',blank='True',upload_to="video/Exercises/%y")
	text=models.TextField(null='True',blank='True')
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	author=models.ForeignKey(User,on_delete=models.CASCADE,null='True',blank='True')	
	class Meta:
		ordering=['-id']
	def __str__(self):
		return str(self.caption)

class EnVideo(models.Model):
	caption=models.CharField(max_length=100)
	video=models.FileField(null='True',blank='True',upload_to="video/Entertainment/%y")
	text=models.TextField(null='True',blank='True')
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	author=models.ForeignKey(User,on_delete=models.CASCADE,null='True',blank='True')
	class Meta:
		ordering=['-id']	
	def __str__(self):
		return str(self.caption)
class EdVideo(models.Model):
	caption=models.CharField(max_length=100)
	video=models.FileField(null='True',blank='True',upload_to="video/Education/%y")
	text=models.TextField(null='True',blank='True')
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	author=models.ForeignKey(User,on_delete=models.CASCADE,null='True',blank='True')
	class Meta:
		ordering=['-id']	
	def __str__(self):
		return str(self.caption)

class SVideo(models.Model):
	caption=models.CharField(max_length=100)
	video=models.FileField(null='True',blank='True',upload_to="video/Sports/%y")
	text=models.TextField(null='True',blank='True')
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	author=models.ForeignKey(User,on_delete=models.CASCADE,null='True',blank='True')
	class Meta:
		ordering=['-id']
	def __str__(self):
		return str(self.caption)

class AgVideo(models.Model):
	caption=models.CharField(max_length=100)
	video=models.FileField(null='True',blank='True',upload_to="video/Agriculture/%y")
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	author=models.ForeignKey(User,on_delete=models.CASCADE,null='True',blank='True')
	class Meta:
		ordering=['-id']	
	def __str__(self):
		return str(self.caption)
class HVideo(models.Model):
	caption=models.CharField(max_length=100)
	video=models.FileField(null='True',blank='True',upload_to="video/Health/%y")
	text=models.TextField(null='True',blank='True')
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	author=models.ForeignKey(User,on_delete=models.CASCADE,null='True',blank='True')
	class Meta:
		ordering=['-id']	
	def __str__(self):
		return str(self.caption)
class TVideo(models.Model):
	caption=models.CharField(max_length=100)
	video=models.FileField(null='True',blank='True',upload_to="video/Tourism/%y")
	text=models.TextField(null='True',blank='True')
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	author=models.ForeignKey(User,on_delete=models.CASCADE,null='True',blank='True')
	class Meta:
		ordering=['-id']	
	def __str__(self):
		return str(self.caption)
class OVideo(models.Model):
	caption=models.CharField(max_length=100)
	video=models.FileField(null='True',blank='True',upload_to="video/Others/%y")
	text=models.TextField(null='True',blank='True')
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	author=models.ForeignKey(User,on_delete=models.CASCADE,null='True',blank='True')
	class Meta:
		ordering=['-id']	
	def __str__(self):
		return str(self.caption)

class DVideo(models.Model):
	caption=models.CharField(max_length=100)
	video=models.FileField(null='True',blank='True',upload_to="video/Devotinal/%y")
	text=models.TextField(null='True',blank='True')
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	author=models.ForeignKey(User,on_delete=models.CASCADE,null='True',blank='True')
	class Meta:
		ordering=['-id']	
	def __str__(self):
		return str(self.caption)

class CoVideo(models.Model):
	caption=models.CharField(max_length=100)
	video=models.FileField(null='True',blank='True',upload_to="video/Cooking/%y")
	text=models.TextField(null='True',blank='True')
	date=models.DateField(auto_now_add=True,blank='True',null='True')
	author=models.ForeignKey(User,on_delete=models.CASCADE,null='True',blank='True')
	class Meta:
		ordering=['-id']	
	def __str__(self):
		return str(self.caption)

class excomment(models.Model):
	exc=models.ForeignKey(ExPost,related_name="excmnt",on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	text=models.TextField()
	date=models.DateTimeField(auto_now_add=True,blank='True',null='True')
	class Meta:
		ordering=['-date']
	def __str__(self):
		return str(self.name)
	def get_absolute_url(self):
		return reverse('ex')

class edcomment(models.Model):
	edc=models.ForeignKey(EdPost,related_name="edcmnt",on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	text=models.TextField()
	date=models.DateTimeField(auto_now_add=True,blank='True',null='True')
	class Meta:
		ordering=['-date']
	def __str__(self):
		return str(self.name)
	def get_absolute_url(self):
		return reverse('ed')

class encomment(models.Model):
	enc=models.ForeignKey(EnPost,related_name="encmnt",on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	text=models.TextField()
	date=models.DateTimeField(auto_now_add=True,blank='True',null='True')
	class Meta:
		ordering=['-date']
	def __str__(self):
		return str(self.name)
	def get_absolute_url(self):
		return reverse('en')

class spcomment(models.Model):
	spc=models.ForeignKey(SPost,related_name="spcmnt",on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	text=models.TextField()
	date=models.DateTimeField(auto_now_add=True,blank='True',null='True')
	class Meta:
		ordering=['-date']
	def __str__(self):
		return str(self.name)
	def get_absolute_url(self):
		return reverse('s')

class agcomment(models.Model):
	agc=models.ForeignKey(AgPost,related_name="agcmnt",on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	text=models.TextField(blank='True',null='True')
	date=models.DateTimeField(auto_now_add=True,blank='True',null='True')
	class Meta:
		ordering=['-date']
	def __str__(self):
		return str(self.name)
	def get_absolute_url(self):
		return reverse('ag')
class tcomment(models.Model):
	tcc=models.ForeignKey(TPost,related_name="tcmnt",on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	text=models.TextField()
	date=models.DateTimeField(auto_now_add=True,blank='True',null='True')
	class Meta:
		ordering=['-date']
	def __str__(self):
		return str(self.name)
	def get_absolute_url(self):
		return reverse('to')
class dcomment(models.Model):
	dc=models.ForeignKey(DPost,related_name="dcmnt",on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	text=models.TextField()
	date=models.DateTimeField(auto_now_add=True,blank='True',null='True')
	class Meta:
		ordering=['-date']
	def __str__(self):
		return str(self.name)
	def get_absolute_url(self):
		return reverse('de')
class hcomment(models.Model):
	hc=models.ForeignKey(HPost,related_name="hcmnt",on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	text=models.TextField()
	date=models.DateTimeField(auto_now_add=True,blank='True',null='True')
	class Meta:
		ordering=['-date']
	def __str__(self):
		return str(self.name)
	def get_absolute_url(self):
		return reverse('he')
class ocomment(models.Model):
	oc=models.ForeignKey(OPost,related_name="ocmnt",on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	text=models.TextField()
	date=models.DateTimeField(auto_now_add=True,blank='True',null='True')
	class Meta:
		ordering=['-date']
	def __str__(self):
		return str(self.name)
	def get_absolute_url(self):
		return reverse('ot')

class Profile(models.Model):
	user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
	bio=models.TextField(default="no bio")
	profile_image=models.ImageField(default="images/default.jpg",null='True',blank='True',upload_to="images/profile_img/")
	following=models.ManyToManyField(User,related_name='following',blank="True")
	def __str__(self):
		return str(self.user)