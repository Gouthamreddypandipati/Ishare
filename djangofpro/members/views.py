from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from .forms import usercreationform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import UsModel
from .forms import UsForm,Editprofilepage,PasswordChangingForm
from django.http import HttpResponseRedirect
from django.contrib.auth.views import PasswordChangeView
'''class userregister(CreateView):
	from_class=UserCreationForm
	template_name ='registration/register.html'
	success_url=reverse_lazy('login')'''



def registerform(request):
	form =usercreationform()
	if request.method =='POST':
		form =usercreationform(request.POST)
		if form.is_valid():
			form.save()
			user=form.cleaned_data.get('username')
			messages.success(request,'ACCOUNT CREATED FOR'+user)
			return redirect('login')
	context ={'form':form}
	return render(request,'registration/register.html',context) 
def loginpage(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('main')
		else:
			messages.info(request, "username or password or incorrect")
	   
	context={}
	return render(request,'registration/login.html',context)
@login_required(login_url='login')	
def logoutpage(request):
	logout(request)
	return redirect('login')

#class AddUs(CreateView):
	#model=UsModel
	#form_class=UsForm
	#template_name='us_forms.html'

class UsView(ListView):
	model=UsModel
	template_name='Userinformation/usl.html'
	ordering=['-id']

def Usdetails_page(request,id):
	obj=get_object_or_404(UsModel,pk=id)
	return render(request,'Userinformation/us_details.html',{'object':obj})

class UsDelete(DeleteView):
	model=UsModel
	template_name='Userinformation/userdel.html'
	success_url=reverse_lazy('main')

class UsUpdate(UpdateView):
	model=UsModel
	template_name='Userinformation/userupd.html'
	fields =['profile_pick','dateofbirth','facebook_id','instagram_id','whatsapp_number','twitter_id','youtubechannel_name','linked_in_profile','yourquote']


def ubase(request):
	return render(request,'Userinformation/userbase.html')



def userpg(request,id): 
	userid=id
	obj=UsModel.objects.filter(author=userid)
	if obj:
		context ={'objects':obj}
		return render(request,'Userinformation/userprflpg.html',context)
	elif request.method =='POST':
		form =UsForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('main')
	else:
		form=UsForm()
	return render(request,'Userinformation/us_forms.html',{'form':form})

class UserEditView(UpdateView):
	form_class=Editprofilepage
	template_name='registration/edit_profile.html'
	success_url=reverse_lazy('main')
	def get_object(self):
		return self.request.user

class PasswordsChangeView(PasswordChangeView):
	form_class=PasswordChangingForm
	success_url=reverse_lazy('password_success')

def password_success(request):
	return render(request,'Passwordreset/password_success.html',{})