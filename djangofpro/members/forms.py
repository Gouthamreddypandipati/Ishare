from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from .models import UsModel

class usercreationform(UserCreationForm):
	class Meta:
		model=User
		fields=['username','email','password1','password2']





class UsForm(forms.ModelForm):
	class Meta:
		model = UsModel
		fields=('author','currentstatus','profile_pick','dateofbirth','facebook_id','instagram_id','whatsapp_number','twitter_id','youtubechannel_name','linked_in_profile','yourquote')

		widgets={
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'usdn','type':'hidden'}),
			'currentstatus' :forms.TextInput(attrs={'class': 'form-control'}),
			'dateofbirth':forms.TextInput(attrs={'class': 'form-control'}),
			'facebook_id':forms.TextInput(attrs={'class': 'form-control'}),
			'instagram_id':forms.TextInput(attrs={'class': 'form-control'}),
			#'whatsapp_number':forms.DecimalField(attrs={'class': 'form-control'}),
			'twitter_id':forms.TextInput(attrs={'class': 'form-control'}),
			'youtubechannel_name':forms.TextInput(attrs={'class': 'form-control'}),
			'linked_in_profile':forms.TextInput(attrs={'class': 'form-control'}),
			'yourquote':forms.TextInput(attrs={'class': 'form-control'}),

		}

class Editprofilepage(UserChangeForm):
	username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
	#last_login=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
	#is_superuser=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	#is_staff=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	#is_active=forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	#date_joined=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
	class Meta:
		model=User
		fields=('username','email','first_name','last_name','password')


class PasswordChangingForm(PasswordChangeForm):
	old_password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
	new_password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','type':'password'}))
	class Meta:
		model=User
		fields=('old_password','new_password1','new_password2')
