from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth.models import User

@receiver(post_save,sender=User)
def auto_profile(created,instance,sender,*args,**kwargs):
	if created:
		Profile.objects.create(user=instance)