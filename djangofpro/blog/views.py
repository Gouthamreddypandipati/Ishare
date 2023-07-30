from django.shortcuts import render,get_object_or_404,HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,View,TemplateView
from . models import ExPost,EdPost,SPost,EnPost,AgPost,EnVideo,ExVideo,EdVideo,SVideo,AgVideo,CoVideo,DVideo,HVideo,OVideo,TVideo,TPost,HPost,DPost,OPost,Profile
from . forms import ExForm,EdForm,SForm,EnForm,HForm,DForm,OForm,TForm,AgForm,EnvForm,ExvForm,EdvForm,SvForm,AgvForm,OvForm,CovForm,TvForm,DvForm,HvForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from . models import excomment,edcomment,encomment,spcomment,agcomment,hcomment,ocomment,dcomment,tcomment
from.forms import ExcmntForm,EdcmntForm,EncmntForm,SpcmntForm,AgcmntForm,ocmntForm,hcmntForm,dcmntForm,tcmntForm
from members.models import UsModel
from django.http import JsonResponse
from itertools import chain
from django.core.paginator import Paginator,EmptyPage
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

class ExView(ListView):
	model=ExPost
	template_name='Exercises/ex.html'
	ordering=['-id']
class TView(ListView):
	model=TPost
	template_name='Tourism/to.html'
	ordering=['-id']
class HView(ListView):
	model=HPost
	template_name='Health/he.html'
	ordering=['-id']
class OView(ListView):
	model=OPost
	template_name='Others/ot.html'
	ordering=['-id']
class DView(ListView):
	model=DPost
	template_name='Devotional/de.html'
	ordering=['-id']
class EdView(ListView):
	model=EdPost
	template_name='Education/ed.html'
	ordering=['-id']
class SView(ListView):
	model=SPost
	template_name='Sports/s.html'	
	ordering=['-id']
class EnView(ListView):
	model=EnPost
	template_name='Entertainment/en.html'
	ordering=['-id']
class AgView(ListView):
	model=AgPost
	context_object_name='agriculture'
	paginate_by=5
	template_name='Agriculture/ag.html'
	ordering=['-id']
@login_required(login_url='login')
def Exdetails_page(request,pk):
	obj=get_object_or_404(ExPost,id=pk)
	return render(request,'Exercises/ex_details.html',{'object':obj})
@login_required(login_url='login')
def Hdetails_page(request,pk):
	obj=get_object_or_404(HPost,id=pk)
	return render(request,'Health/he_details.html',{'object':obj})
@login_required(login_url='login')
def Ddetails_page(request,pk):
	obj=get_object_or_404(DPost,id=pk)
	return render(request,'Devotional/de_details.html',{'object':obj})
@login_required(login_url='login')
def Odetails_page(request,pk):
	obj=get_object_or_404(OPost,id=pk)
	return render(request,'Others/ot_details.html',{'object':obj})
@login_required(login_url='login')
def Tdetails_page(request,pk):
	obj=get_object_or_404(TPost,id=pk)
	return render(request,'Tourism/to_details.html',{'object':obj})
@login_required(login_url='login')
def Eddetails_page(request,pk):
	obj=get_object_or_404(EdPost,id=pk)
	return render(request,'Education/ed_details.html',{'object':obj})
@login_required(login_url='login')
def Sdetails_page(request,pk):
	obj=get_object_or_404(SPost,id=pk)
	return render(request,'Sports/s_details.html',{'object':obj})
@login_required(login_url='login')
def Endetails_page(request,pk):
	obj=get_object_or_404(EnPost,id=pk)
	return render(request,'Entertainment/en_details.html',{'object':obj})
@login_required(login_url='login')
def Agdetails_page(request,pk):
	obj=get_object_or_404(AgPost,id=pk)
	return render(request,'Agriculture/ag_details.html',{'object':obj})
@login_required(login_url='login')
def main(request):
	return render(request,'main.html',{})
@login_required(login_url='login')
def ADDP(request):
	return render(request,'ADDPOST.html')
class AddEX(CreateView):
	model=ExPost
	form_class=ExForm
	template_name='Exercises/ex_form.html'
class AddH(CreateView):
	model=HPost
	form_class=HForm
	template_name='Health/he_form.html'
class AddT(CreateView):
	model=TPost
	form_class=TForm
	template_name='Tourism/to_form.html'
class AddO(CreateView):
	model=OPost
	form_class=OForm
	template_name='Others/ot_form.html'
class AddD(CreateView):
	model=DPost
	form_class=DForm
	template_name='Devotional/de_form.html'
class AddEd(CreateView):
	model=EdPost
	form_class=EdForm
	template_name='Education/ed_form.html'

class AddS(CreateView):
	model=SPost
	form_class=SForm
	template_name='Sports/s_form.html'

class AddEn(CreateView):
	model=EnPost
	form_class=EnForm
	template_name='Entertainment/en_form.html'

class AddAg(CreateView):
	model=AgPost
	form_class=AgForm
	template_name='Agriculture/ag_form.html'


class EdUpdate(UpdateView):
	model=EdPost
	form_class=EdForm
	template_name='Education/ed_update.html'

class EdDelete(DeleteView):
	model=EdPost
	template_name='Education/ed_delete.html'
	success_url=reverse_lazy('main')
class TUpdate(UpdateView):
	model=TPost
	form_class=HForm
	template_name='Tourism/to_update.html'

class TDelete(DeleteView):
	model=TPost
	template_name='Tourism/to_delete.html'
	success_url=reverse_lazy('main')

class HUpdate(UpdateView):
	model=HPost
	form_class=HForm
	template_name='Health/he_update.html'
	

class HDelete(DeleteView):
	model=HPost
	template_name='Health/he_delete.html'
	success_url=reverse_lazy('main')
class OUpdate(UpdateView):
	model=OPost
	form_class=OForm
	template_name='Others/ot_update.html'

class ODelete(DeleteView):
	model=OPost
	template_name='Others/ot_delete.html'
	success_url=reverse_lazy('main')
class DUpdate(UpdateView):
	model=DPost
	form_class=DForm
	template_name='Devotional/de_update.html'

class DDelete(DeleteView):
	model=DPost
	template_name='Devotional/de_delete.html'
	success_url=reverse_lazy('main')
class ExUpdate(UpdateView):
	model=ExPost
	form_class=ExForm
	template_name='Exercises/ex_update.html'

class ExDelete(DeleteView):
	model=ExPost
	template_name='Exercises/ex_delete.html'
	success_url=reverse_lazy('main')


class SUpdate(UpdateView):
	model=SPost
	form_class=SForm
	template_name='Sports/s_update.html'

class SDelete(DeleteView):
	model=SPost
	template_name='Sports/s_delete.html'
	success_url=reverse_lazy('main')


class EnUpdate(UpdateView):
	model=EnPost
	form_class=EnForm
	template_name='Entertainment/en_update.html'

class EnDelete(DeleteView):
	model=EnPost
	template_name='Entertainment/en_delete.html'
	success_url=reverse_lazy('main')

class AgUpdate(UpdateView):
	model=AgPost
	form_class=AgForm
	template_name='Agriculture/ag_update.html'
	#fields =['title','text','header_image']

class AgDelete(DeleteView):
	model=AgPost
	template_name='Agriculture/ag_delete.html'
	success_url=reverse_lazy('main')

def Exvideo(request):
	if request.method=='POST':
		form=ExvForm(data=request.POST,files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'FORM UPLOADED SUCCESSFULLY')
			return HttpResponseRedirect(reverse('exv'))
		else:
			messages.Failed(request,'upss... something went wrong')
	else:
		form=ExvForm()
	return render(request,'Exercises/exv.html',{'form':form})

def Hvideo(request):
	if request.method=='POST':
		form=HvForm(data=request.POST,files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'FORM UPLOADED SUCCESSFULLY')
			return HttpResponseRedirect(reverse('hev'))
		else:
			messages.Failed(request,'upss... something went wrong')
	else:
		form=HvForm()
	return render(request,'Health/hev.html',{'form':form})
def Dvideo(request):
	if request.method=='POST':
		form=DvForm(data=request.POST,files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'FORM UPLOADED SUCCESSFULLY')
			return HttpResponseRedirect(reverse('dev'))
		else:
			messages.Failed(request,'upss... something went wrong')
	else:
		form=DvForm()
	return render(request,'Devotional/dev.html',{'form':form})
def Tvideo(request):
	if request.method=='POST':
		form=TvForm(data=request.POST,files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'FORM UPLOADED SUCCESSFULLY')
			return HttpResponseRedirect(reverse('tov'))
		else:
			messages.Failed(request,'upss... something went wrong')
	else:
		form=TvForm()
	return render(request,'Tourism/tov.html',{'form':form})
def Covideo(request):
	if request.method=='POST':
		form=CovForm(data=request.POST,files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'FORM UPLOADED SUCCESSFULLY')
			return HttpResponseRedirect(reverse('cov'))
		else:
			messages.Failed(request,'upss... something went wrong')
	else:
		form=CovForm()
	return render(request,'Cooking/cov.html',{'form':form})
def Ovideo(request):
	if request.method=='POST':
		form=OvForm(data=request.POST,files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'FORM UPLOADED SUCCESSFULLY')
			return HttpResponseRedirect(reverse('otv'))
		else:
			messages.Failed(request,'upss... something went wrong')
	else:
		form=OvForm()
	return render(request,'Others/otv.html',{'form':form})
def Exvideowatch(request):
	all_video=ExVideo.objects.all()
	all_video.order_by('-id')
	return render(request,'Exercises/exvwatch.html',{"all":all_video})
def Tvideowatch(request):
	all_video=TVideo.objects.all()
	all_video.order_by('-id')
	return render(request,'Tourism/tovwatch.html',{"all":all_video})
def Dvideowatch(request):
	all_video=DVideo.objects.all()
	all_video.order_by('-id')
	return render(request,'Devotional/devwatch.html',{"all":all_video})
def Hvideowatch(request):
	all_video=HVideo.objects.all()
	all_video.order_by('-id')
	return render(request,'Health/hevwatch.html',{"all":all_video})
def Ovideowatch(request):
	all_video=OVideo.objects.all()
	all_video.order_by('-id')
	return render(request,'Others/otvwatch.html',{"all":all_video})
def Covideowatch(request):
	all_video=CoVideo.objects.all()
	all_video.order_by('-id')
	return render(request,'Cooking/covwatch.html',{"all":all_video})
def Envideo(request):
	if request.method=='POST':
		form=EnvForm(data=request.POST,files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'FORM UPLOADED SUCCESSFULLY')
			return HttpResponseRedirect(reverse('env'))
		else:
			messages.Failed(request,'upss... something went wrong')
	else:
		form=EnvForm()
	return render(request,'Entertainment/env.html',{'form':form})
def Envideowatch(request):
	all_video=EnVideo.objects.all()
	all_video.order_by('id')
	return render(request,'Entertainment/envwatch.html',{"all":all_video})
def Edvideo(request):
	if request.method=='POST':
		form=EdvForm(data=request.POST,files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'FORM UPLOADED SUCCESSFULLY')
			return HttpResponseRedirect(reverse('edv'))
		else:
			messages.Failed(request,'upss... something went wrong')
	
	else:
		form=EdvForm()
	return render(request,'Education/edv.html',{'form':form})

def Edvideowatch(request):
	all_video=EdVideo.objects.all()
	return render(request,'Education/edvwatch.html',{"all":all_video})	

def Svideo(request):
	if request.method=='POST':
		form=SvForm(data=request.POST,files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'FORM UPLOADED SUCCESSFULLY')
			return HttpResponseRedirect(reverse('sv'))
		else:
			messages.Failed(request,'upss... something went wrong')
	else:
		form=SvForm()
	return render(request,'Sports/sv.html',{'form':form})

def Spvideowatch(request):
	all_video=SVideo.objects.all()
	return render(request,'Sports/svwatch.html',{"all":all_video})

def Agvideo(request):
	if request.method=='POST':
		form=AgvForm(data=request.POST,files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'FORM UPLOADED SUCCESSFULLY')
			return HttpResponseRedirect(reverse('agv'))
		else:
			messages.Failed(request,'upss... something went wrong')
	else:
		form=AgvForm()
	return render(request,'Agriculture/agv.html',{"form":form})

def Agvideowatch(request):
	all_video=AgVideo.objects.all()
	return render(request,'Agriculture/agvwatch.html',{"all":all_video})	

#lik dislik for ex
def likeviewex(request,pk):
	lik=get_object_or_404(ExPost,id=pk)
	liked=False
	if lik.likes.filter(id=request.user.id).exists():
		lik.likes.remove(request.user)
		liked=False
	elif lik.dislikes.filter(id=request.user.id).exists():
		lik.dislikes.remove(request.user)
		lik.likes.add(request.user)
		liked=True
	else:
		lik.likes.add(request.user)
		liked=True
	datalik={
	'likes':lik.likes.all().count(),
	'dislikes':lik.dislikes.all().count(),
	'liked':liked
	}
	return JsonResponse(datalik,safe=False)

def dislikeviewex(request,pk):
	dislik=get_object_or_404(ExPost,id=pk)
	disliked=False
	if dislik.dislikes.filter(id=request.user.id).exists():
		dislik.dislikes.remove(request.user)
		disliked=False
	elif dislik.likes.filter(id=request.user.id).exists():
		dislik.likes.remove(request.user)
		dislik.dislikes.add(request.user)
		disliked=True
	else:
		dislik.dislikes.add(request.user)
		disliked=True
	datadislik={
	'likes':dislik.likes.all().count(),
	'dislik':dislik.dislikes.all().count(),
	'disliked':disliked
	}
	return JsonResponse(datadislik,safe=False)
#likdislik for health section
def likeviewhe(request,pk):
	lik=get_object_or_404(HPost,id=pk)
	liked=False
	if lik.likes.filter(id=request.user.id).exists():
		lik.likes.remove(request.user)
		liked=False
	elif lik.dislikes.filter(id=request.user.id).exists():
		lik.dislikes.remove(request.user)
		lik.likes.add(request.user)
		liked=True
	else:
		lik.likes.add(request.user)
		liked=True
	datalik={
	'likes':lik.likes.all().count(),
	'dislikes':lik.dislikes.all().count(),
	'liked':liked
	}
	return JsonResponse(datalik,safe=False)

def dislikeviewhe(request,pk):
	dislik=get_object_or_404(HPost,id=pk)
	disliked=False
	if dislik.dislikes.filter(id=request.user.id).exists():
		dislik.dislikes.remove(request.user)
		disliked=False
	elif dislik.likes.filter(id=request.user.id).exists():
		dislik.likes.remove(request.user)
		dislik.dislikes.add(request.user)
		disliked=True
	else:
		dislik.dislikes.add(request.user)
		disliked=True
	datadislik={
	'likes':dislik.likes.all().count(),
	'dislik':dislik.dislikes.all().count(),
	'disliked':disliked
	}
	return JsonResponse(datadislik,safe=False)
# lik dis like for ed
def likeviewed(request,pk):
	lik=get_object_or_404(EdPost,id=pk)
	liked=False
	if lik.likes.filter(id=request.user.id).exists():
		lik.likes.remove(request.user)
		liked=False
	elif lik.dislikes.filter(id=request.user.id).exists():
		lik.dislikes.remove(request.user)
		lik.likes.add(request.user)
		liked=True
	else:
		lik.likes.add(request.user)
		liked=True
	datalik={
	'likes':lik.likes.all().count(),
	'dislikes':lik.dislikes.all().count(),
	'liked':liked
	}
	return JsonResponse(datalik,safe=False)
def dislikeviewed(request,pk):
	dislik=get_object_or_404(EdPost,id=pk)
	disliked=False
	if dislik.dislikes.filter(id=request.user.id).exists():
		dislik.dislikes.remove(request.user)
		disliked=False
	elif dislik.likes.filter(id=request.user.id).exists():
		dislik.likes.remove(request.user)
		dislik.dislikes.add(request.user)
		disliked=True
	else:
		dislik.dislikes.add(request.user)
		disliked=True
	datadislik={
	'likes':dislik.likes.all().count(),
	'dislik':dislik.dislikes.all().count(),
	'disliked':disliked
	}
	return JsonResponse(datadislik,safe=False)
#likes dis likes for ot
def likeviewot(request,pk):
	lik=get_object_or_404(OPost,id=pk)
	liked=False
	if lik.likes.filter(id=request.user.id).exists():
		lik.likes.remove(request.user)
		liked=False
	elif lik.dislikes.filter(id=request.user.id).exists():
		lik.dislikes.remove(request.user)
		lik.likes.add(request.user)
		liked=True
	else:
		lik.likes.add(request.user)
		liked=True
	datalik={
	'likes':lik.likes.all().count(),
	'dislikes':lik.dislikes.all().count(),
	'liked':liked
	}
	return JsonResponse(datalik,safe=False)

def dislikeviewot(request,pk):
	dislik=get_object_or_404(OPost,id=pk)
	disliked=False
	if dislik.dislikes.filter(id=request.user.id).exists():
		dislik.dislikes.remove(request.user)
		disliked=False
	elif dislik.likes.filter(id=request.user.id).exists():
		dislik.likes.remove(request.user)
		dislik.dislikes.add(request.user)
		disliked=True
	else:
		dislik.dislikes.add(request.user)
		disliked=True
	datadislik={
	'likes':dislik.likes.all().count(),
	'dislik':dislik.dislikes.all().count(),
	'disliked':disliked
	}
	return JsonResponse(datadislik,safe=False)
# lk vwe for tourism
def likeviewto(request,pk):
	lik=get_object_or_404(TPost,id=pk)
	liked=False
	if lik.likes.filter(id=request.user.id).exists():
		lik.likes.remove(request.user)
		liked=False
	elif lik.dislikes.filter(id=request.user.id).exists():
		lik.dislikes.remove(request.user)
		lik.likes.add(request.user)
		liked=True
	else:
		lik.likes.add(request.user)
		liked=True
	datalik={
	'likes':lik.likes.all().count(),
	'dislikes':lik.dislikes.all().count(),
	'liked':liked
	}
	return JsonResponse(datalik,safe=False)
def dislikeviewto(request,pk):
	dislik=get_object_or_404(TPost,id=pk)
	disliked=False
	if dislik.dislikes.filter(id=request.user.id).exists():
		dislik.dislikes.remove(request.user)
		disliked=False
	elif dislik.likes.filter(id=request.user.id).exists():
		dislik.likes.remove(request.user)
		dislik.dislikes.add(request.user)
		disliked=True
	else:
		dislik.dislikes.add(request.user)
		disliked=True
	datadislik={
	'likes':dislik.likes.all().count(),
	'dislik':dislik.dislikes.all().count(),
	'disliked':disliked
	}
	return JsonResponse(datadislik,safe=False)
# lik dis like for en
def likeviewen(request,pk):
	lik=get_object_or_404(EnPost,id=pk)
	liked=False
	if lik.likes.filter(id=request.user.id).exists():
		lik.likes.remove(request.user)
		liked=False
	elif lik.dislikes.filter(id=request.user.id).exists():
		lik.dislikes.remove(request.user)
		lik.likes.add(request.user)
		liked=True
	else:
		lik.likes.add(request.user)
		liked=True
	datalik={
	'likes':lik.likes.all().count(),
	'dislikes':lik.dislikes.all().count(),
	'liked':liked
	}
	return JsonResponse(datalik,safe=False)
def dislikeviewen(request,pk):
	dislik=get_object_or_404(EnPost,id=pk)
	disliked=False
	if dislik.dislikes.filter(id=request.user.id).exists():
		dislik.dislikes.remove(request.user)
		disliked=False
	elif dislik.likes.filter(id=request.user.id).exists():
		dislik.likes.remove(request.user)
		dislik.dislikes.add(request.user)
		disliked=True
	else:
		dislik.dislikes.add(request.user)
		disliked=True
	datadislik={
	'likes':dislik.likes.all().count(),
	'dislik':dislik.dislikes.all().count(),
	'disliked':disliked
	}
	return JsonResponse(datadislik,safe=False)
#lik and dis like for sports
def likeviewsp(request,pk):
	lik=get_object_or_404(SPost,id=pk)
	liked=False
	if lik.likes.filter(id=request.user.id).exists():
		lik.likes.remove(request.user)
		liked=False
	elif lik.dislikes.filter(id=request.user.id).exists():
		lik.dislikes.remove(request.user)
		lik.likes.add(request.user)
		liked=True
	else:
		lik.likes.add(request.user)
		liked=True
	datalik={
	'likes':lik.likes.all().count(),
	'dislikes':lik.dislikes.all().count(),
	'liked':liked
	}
	return JsonResponse(datalik,safe=False)
def dislikeviewsp(request,pk):
	dislik=get_object_or_404(SPost,id=pk)
	disliked=False
	if dislik.dislikes.filter(id=request.user.id).exists():
		dislik.dislikes.remove(request.user)
		disliked=False
	elif dislik.likes.filter(id=request.user.id).exists():
		dislik.likes.remove(request.user)
		dislik.dislikes.add(request.user)
		disliked=True
	else:
		dislik.dislikes.add(request.user)
		disliked=True
	datadislik={
	'likes':dislik.likes.all().count(),
	'dislik':dislik.dislikes.all().count(),
	'disliked':disliked
	}
	return JsonResponse(datadislik,safe=False)



#lik dislik view for ag
def likeviewag(request,pk):
	lik=get_object_or_404(AgPost,id=pk)
	liked=False
	if lik.likes.filter(id=request.user.id).exists():
		lik.likes.remove(request.user)
		liked=False
	elif lik.dislikes.filter(id=request.user.id).exists():
		lik.dislikes.remove(request.user)
		lik.likes.add(request.user)
		liked=True
	else:
		lik.likes.add(request.user)
		liked=True
	datalik={
	'likes':lik.likes.all().count(),
	'dislikes':lik.dislikes.all().count(),
	'liked':liked
	}
	return JsonResponse(datalik,safe=False)

def dislikeviewag(request,pk):
	dislik=get_object_or_404(AgPost,id=pk)
	disliked=False
	if dislik.dislikes.filter(id=request.user.id).exists():
		dislik.dislikes.remove(request.user)
		disliked=False
	elif dislik.likes.filter(id=request.user.id).exists():
		dislik.likes.remove(request.user)
		dislik.dislikes.add(request.user)
		disliked=True
	else:
		dislik.dislikes.add(request.user)
		disliked=True
	datadislik={
	'likes':dislik.likes.all().count(),
	'dislik':dislik.dislikes.all().count(),
	'disliked':disliked
	}
	return JsonResponse(datadislik,safe=False)
# lik and dislike for devotions
def likeviewde(request,pk):
	lik=get_object_or_404(DPost,id=pk)
	liked=False
	if lik.likes.filter(id=request.user.id).exists():
		lik.likes.remove(request.user)
		liked=False
	elif lik.dislikes.filter(id=request.user.id).exists():
		lik.dislikes.remove(request.user)
		lik.likes.add(request.user)
		liked=True
	else:
		lik.likes.add(request.user)
		liked=True
	datalik={
	'likes':lik.likes.all().count(),
	'dislikes':lik.dislikes.all().count(),
	'liked':liked
	}
	return JsonResponse(datalik,safe=False)
def dislikeviewde(request,pk):
	dislik=get_object_or_404(DPost,id=pk)
	disliked=False
	if dislik.dislikes.filter(id=request.user.id).exists():
		dislik.dislikes.remove(request.user)
		disliked=False
	elif dislik.likes.filter(id=request.user.id).exists():
		dislik.likes.remove(request.user)
		dislik.dislikes.add(request.user)
		disliked=True
	else:
		dislik.dislikes.add(request.user)
		disliked=True
	datadislik={
	'likes':dislik.likes.all().count(),
	'dislik':dislik.dislikes.all().count(),
	'disliked':disliked
	}
	return JsonResponse(datadislik,safe=False)

def Exposts_page(request,id):
	userid=id
	userposts=ExPost.objects.filter(author=userid)
	return render(request,'Exercises/ex_posts.html',{'userposts':userposts})
	ordering=['-id']
def Dposts_page(request,id):
	userid=id
	userposts=DPost.objects.filter(author=userid)
	return render(request,'Devotional/de_posts.html',{'userposts':userposts})
	ordering=['-id']
def Hposts_page(request,id):
	userid=id
	userposts=HPost.objects.filter(author=userid)
	return render(request,'Health/he_posts.html',{'userposts':userposts})
	ordering=['-id']
def Tposts_page(request,id):
	userid=id
	userposts=TPost.objects.filter(author=userid)
	return render(request,'Tourism/to_posts.html',{'userposts':userposts})
	ordering=['-id']
def Oposts_page(request,id):
	userid=id
	userposts=OPost.objects.filter(author=userid)
	return render(request,'Others/ot_posts.html',{'userposts':userposts})
	ordering=['-id']

def Enposts_page(request,id):
	userid=id
	userposts=EnPost.objects.filter(author=userid)
	return render(request,'Entertainment/en_posts.html',{'userposts':userposts})

def Agposts_page(request,id):
	userid=id
	userposts=AgPost.objects.filter(author=userid)
	return render(request,'Agriculture/ag_posts.html',{'userposts':userposts})

def Edposts_page(request,id):
	userid=id
	userposts=EdPost.objects.filter(author=userid)
	return render(request,'Education/ed_posts.html',{'userposts':userposts})

def Sposts_page(request,id):
	userid=id
	userposts=SPost.objects.filter(author=userid)
	return render(request,'Sports/s_posts.html',{'userposts':userposts})

### excomment
@csrf_exempt
def ExComment(request,pk):
	if request.method=='POST':
		name=request.user.username
		exc_id=pk
		text=request.POST.get('comment')
		excomment.objects.create(name=name, text=text,exc_id=pk)
		return HttpResponseRedirect(reverse('ex_details',args=[str(pk)]))
def ExCommentForm(request):
	form=ExcmntForm()
	return render(request,"Exercises/ex_details.html",{"form":form})
###
### hcomment
@csrf_exempt
def HComment(request,pk):
	if request.method=='POST':
		name=request.user.username
		hc_id=pk
		text=request.POST.get('comment')
		hcomment.objects.create(name=name, text=text,hc_id=pk)
		return HttpResponseRedirect(reverse('he_details',args=[str(pk)]))
def HCommentForm(request):
	form=hcmntForm()
	return render(request,"Health/he_details.html",{"form":form})
###
### Dcomment
@csrf_exempt
def DComment(request,pk):
	if request.method=='POST':
		name=request.user.username
		d_id=pk
		text=request.POST.get('comment')
		dcomment.objects.create(name=name, text=text,dc_id=pk)
		return HttpResponseRedirect(reverse('de_details',args=[str(pk)]))
def DCommentForm(request):
	form=dcmntForm()
	return render(request,"Devotional/de_details.html",{"form":form})
###
### othercomment
@csrf_exempt
def OComment(request,pk):
	if request.method=='POST':
		name=request.user.username
		o_id=pk
		text=request.POST.get('comment')
		ocomment.objects.create(name=name, text=text,oc_id=pk)
		return HttpResponseRedirect(reverse('ot_details',args=[str(pk)]))
def OCommentForm(request):
	form=ocmntForm()
	return render(request,"Others/ot_details.html",{"form":form})
###
### tcomment
@csrf_exempt
def TComment(request,pk):
	if request.method=='POST':
		name=request.user.username
		t_id=pk
		text=request.POST.get('comment')
		tcomment.objects.create(name=name, text=text,tcc_id=pk)
		return HttpResponseRedirect(reverse('to_details',args=[str(pk)]))
def TCommentForm(request):
	form=tcmntForm()
	return render(request,"Tourism/to_details.html",{"form":form})
###
### educationcomment
@csrf_exempt
def EdComment(request,pk):
	if request.method=='POST':
		name=request.user.username
		e_id=pk
		text=request.POST.get('comment')
		edcomment.objects.create(name=name, text=text,edc_id=pk)
		return HttpResponseRedirect(reverse('ed_details',args=[str(pk)]))
def EdCommentForm(request):
	form=EdcmntForm()
	return render(request,"Education/ed_details.html",{"form":form})
###
### entertainmentcomment
@csrf_exempt
def EnComment(request,pk):
	if request.method=='POST':
		name=request.user.username
		en_id=pk
		text=request.POST.get('comment')
		encomment.objects.create(name=name, text=text,enc_id=pk)
		return HttpResponseRedirect(reverse('en_details',args=[str(pk)]))
def EnCommentForm(request):
	form=EncmntForm()
	return render(request,"Entertainment/en_details.html",{"form":form})
###
### sportscomment
@csrf_exempt
def SpComment(request,pk):
	if request.method=='POST':
		name=request.user.username
		s_id=pk
		text=request.POST.get('comment')
		spcomment.objects.create(name=name, text=text,spc_id=pk)
		return HttpResponseRedirect(reverse('s_details',args=[str(pk)]))
def SpCommentForm(request):
	form=SpcmntForm()
	return render(request,"Sports/s_details.html",{"form":form})
###
### agriculture comment
@csrf_exempt
def AgComment(request,pk):
	if request.method=='POST':
		name=request.user.username
		agc_id=pk
		text=request.POST.get('comment')
		agcomment.objects.create(name=name, text=text,agc_id=pk)
		return HttpResponseRedirect(reverse('ag_details',args=[str(pk)]))
def AgCommentForm(request):
	form=AgcmntForm()
	return render(request,"Agriculture/ag_details.html",{"form":form})


def exvupdate(request,pk):
	order=ExVideo.objects.get(id=pk)
	form=ExvForm(instance=order)
	if request.method=='POST':
		form=ExvForm(data=request.POST,files=request.FILES,instance=order)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('exvw'))
	context={'form':form}
	return render(request,'Exercises/exv_update.html',context)
def exvdelete(request,pk):
	order=ExVideo.objects.get(id=pk)
	if request.method=='POST':
		order.delete()
		return HttpResponseRedirect(reverse('exvw'))
	context={'iteam':order}
	return render(request,'Exercises/exv_delete.html',context)
def Exvideos_page(request,id):
	userid=id
	uservideos=ExVideo.objects.filter(author=userid)
	return render(request,'Exercises/ex_videos.html',{'uservideos':uservideos})
	ordering=['-id']

def tvupdate(request,pk):
	order=TVideo.objects.get(id=pk)
	form=TvForm(instance=order)
	if request.method=='POST':
		form=TvForm(data=request.POST,files=request.FILES,instance=order)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('tovw'))
	context={'form':form}
	return render(request,'Tourism/tov_update.html',context)
def tvdelete(request,pk):
	order=TVideo.objects.get(id=pk)
	if request.method=='POST':
		order.delete()
		return HttpResponseRedirect(reverse('tovw'))
	context={'iteam':order}
	return render(request,'Tourism/tov_delete.html',context)
def Tvideos_page(request,id):
	userid=id
	uservideos=TVideo.objects.filter(author=userid)
	return render(request,'Tourism/to_videos.html',{'uservideos':uservideos})
	ordering=['-id']
def ovupdate(request,pk):
	order=OVideo.objects.get(id=pk)
	form=OvForm(instance=order)
	if request.method=='POST':
		form=OvForm(data=request.POST,files=request.FILES,instance=order)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('otvw'))
	context={'form':form}
	return render(request,'Others/otv_update.html',context)
def ovdelete(request,pk):
	order=OVideo.objects.get(id=pk)
	if request.method=='POST':
		order.delete()
		return HttpResponseRedirect(reverse('otvw'))
	context={'iteam':order}
	return render(request,'Others/otv_delete.html',context)
def Ovideos_page(request,id):
	userid=id
	uservideos=OVideo.objects.filter(author=userid)
	return render(request,'Others/ot_videos.html',{'uservideos':uservideos})
	ordering=['-id']
def hvupdate(request,pk):
	order=HVideo.objects.get(id=pk)
	form=HvForm(instance=order)
	if request.method=='POST':
		form=HvForm(data=request.POST,files=request.FILES,instance=order)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('hevw'))
	context={'form':form}
	return render(request,'Health/hev_update.html',context)
def hvdelete(request,pk):
	order=HVideo.objects.get(id=pk)
	if request.method=='POST':
		order.delete()
		return HttpResponseRedirect(reverse('hevw'))
	context={'iteam':order}
	return render(request,'Health/hev_delete.html',context)
def Hvideos_page(request,id):
	userid=id
	uservideos=HVideo.objects.filter(author=userid)
	return render(request,'Health/he_videos.html',{'uservideos':uservideos})
	ordering=['-id']
def dvupdate(request,pk):
	order=DVideo.objects.get(id=pk)
	form=DvForm(instance=order)
	if request.method=='POST':
		form=DvForm(data=request.POST,files=request.FILES,instance=order)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('devw'))
	context={'form':form}
	return render(request,'Devotional/dev_update.html',context)
def dvdelete(request,pk):
	order=DVideo.objects.get(id=pk)
	if request.method=='POST':
		order.delete()
		return HttpResponseRedirect(reverse('devw'))
	context={'iteam':order}
	return render(request,'Devotional/dev_delete.html',context)
def Dvideos_page(request,id):
	userid=id
	uservideos=DVideo.objects.filter(author=userid)
	return render(request,'Devotional/de_videos.html',{'uservideos':uservideos})
	ordering=['-id']
def covupdate(request,pk):
	order=CoVideo.objects.get(id=pk)
	form=CovForm(instance=order)
	if request.method=='POST':
		form=CovForm(data=request.POST,files=request.FILES,instance=order)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('covw'))
	context={'form':form}
	return render(request,'Cooking/cov_update.html',context)
def covdelete(request,pk):
	order=CoVideo.objects.get(id=pk)
	if request.method=='POST':
		order.delete()
		return HttpResponseRedirect(reverse('covw'))
	context={'iteam':order}
	return render(request,'Cooking/cov_delete.html',context)
def Covideos_page(request,id):
	userid=id
	uservideos=CoVideo.objects.filter(author=userid)
	return render(request,'Cooking/co_videos.html',{'uservideos':uservideos})
	ordering=['-id']
def edvupdate(request,pk):
	order=EdVideo.objects.get(id=pk)
	form=EdvForm(instance=order)
	if request.method=='POST':
		form=EdvForm(data=request.POST,files=request.FILES,instance=order)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('edvw'))
	context={'form':form}
	return render(request,'Education/edv_update.html',context)
def edvdelete(request,pk):
	order=EdVideo.objects.get(id=pk)
	if request.method=='POST':
		order.delete()
		return HttpResponseRedirect(reverse('edvw'))
	context={'iteam':order}
	return render(request,'Education/edv_delete.html',context)
def Edvideos_page(request,id):
	userid=id
	uservideos=EdVideo.objects.filter(author=userid)
	return render(request,'Education/ed_videos.html',{'uservideos':uservideos})
	ordering=['-id']

def envupdate(request,pk):
	order=EnVideo.objects.get(id=pk)
	form=EnvForm(instance=order)
	if request.method=='POST':
		form=EnvForm(data=request.POST,files=request.FILES,instance=order)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('envw'))
	context={'form':form}
	return render(request,'Entertainment/env_update.html',context)
def envdelete(request,pk):
	order=EnVideo.objects.get(id=pk)
	if request.method=='POST':
		order.delete()
		return HttpResponseRedirect(reverse('envw'))
	context={'iteam':order}
	return render(request,'Entertainment/env_delete.html',context)
def Envideos_page(request,id):
	userid=id
	uservideos=EnVideo.objects.filter(author=userid)
	return render(request,'Entertainment/en_videos.html',{'uservideos':uservideos})
	ordering=['-id']
def spvupdate(request,pk):
	order=SVideo.objects.get(id=pk)
	form=SvForm(instance=order)
	if request.method=='POST':
		form=SvForm(data=request.POST,files=request.FILES,instance=order)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('spvw'))
	context={'form':form}
	return render(request,'Sports/spv_update.html',context)
def spvdelete(request,pk):
	order=SVideo.objects.get(id=pk)
	if request.method=='POST':
		order.delete()
		return HttpResponseRedirect(reverse('spvw'))
	context={'iteam':order}
	return render(request,'Sports/spv_delete.html',context)
def Spvideos_page(request,id):
	userid=id
	uservideos=SVideo.objects.filter(author=userid)
	return render(request,'Sports/sp_videos.html',{'uservideos':uservideos})
	ordering=['-id']

def agvupdate(request,pk):
	order=AgVideo.objects.get(id=pk)
	form=AgvForm(instance=order)
	if request.method=='POST':
		form=AgvForm(data=request.POST,files=request.FILES,instance=order)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('agvw'))
	context={'form':form}
	return render(request,'Agriculture/agv_update.html',context)
def agvdelete(request,pk):
	order=AgVideo.objects.get(id=pk)
	if request.method=='POST':
		order.delete()
		return HttpResponseRedirect(reverse('agvw'))
	context={'iteam':order}
	return render(request,'Agriculture/agv_delete.html',context)
def Agvideos_page(request,id):
	userid=id
	uservideos=AgVideo.objects.filter(author=userid)
	return render(request,'Agriculture/ag_videos.html',{'uservideos':uservideos})

def search(request):
	if request.method=='GET':
		query=request.GET.get('querys')
		allpoststitleex=ExPost.objects.filter(title__icontains=query)
		allpostsuserex=ExPost.objects.filter(author__username__icontains=query)
		allpoststitleen=EnPost.objects.filter(title__icontains=query)
		allpostsuseren=EnPost.objects.filter(author__username__icontains=query)
		allpoststitleed=EdPost.objects.filter(title__icontains=query)
		allpostsusered=EdPost.objects.filter(author__username__icontains=query)
		allpoststitles=SPost.objects.filter(title__icontains=query)
		allpostsusers=SPost.objects.filter(author__username__icontains=query)
		allpoststitleag=AgPost.objects.filter(title__icontains=query)
		allpostsuserag=AgPost.objects.filter(author__username__icontains=query)
		allpoststitlet=TPost.objects.filter(title__icontains=query)
		allpostsusert=TPost.objects.filter(author__username__icontains=query)
		allpoststitled=DPost.objects.filter(title__icontains=query)
		allpostsuserd=DPost.objects.filter(author__username__icontains=query)
		allpoststitleo=OPost.objects.filter(title__icontains=query)
		allpostsusero=OPost.objects.filter(author__username__icontains=query)
		allpoststitleh=HPost.objects.filter(title__icontains=query)
		allpostsuserh=HPost.objects.filter(author__username__icontains=query)
		allpostsex=allpoststitleex.union(allpostsuserex)
		allpostsh=allpoststitleh.union(allpostsuserh)
		allpostso=allpoststitleo.union(allpostsusero)
		allpostst=allpoststitlet.union(allpostsusert)
		allpostsd=allpoststitled.union(allpostsuserd)
		allpostsen=allpoststitleen.union(allpostsuseren)
		allpostsed=allpoststitleed.union(allpostsusered)
		allpostss=allpoststitles.union(allpostsusers)
		allpostsag=allpoststitleag.union(allpostsuserag)
		return render(request,'search.html',{'allpostsex':allpostsex,'allpostsen':allpostsen,'allpostsed':allpostsed,'allpostss':allpostss,'allpostsag':allpostsag,'allpostsh':allpostsh,'allpostso':allpostso,'allpostst':allpostst,'allpostsd':allpostsd})


def searchcov(request):
	if request.method=='GET':
		queryco=request.GET.get('coquerys')
		allpoststitlecov=CoVideo.objects.filter(author__username__icontains=queryco)	
		return render(request,'Cooking/cosearch.html',{'allpoststitlecov':allpoststitlecov})

def searchent(request):
	if request.method=='GET':
		queryent=request.GET.get('entquerys')
		allpoststitleent=EnVideo.objects.filter(author__username__icontains=queryent)
		return render(request,'Entertainment/ensearch.html',{'allpoststitleent':allpoststitleent})

def searchagr(request):
	if request.method=='GET':
		queryagr=request.GET.get('agrquerys')
		allpostsuseragr=AgVideo.objects.filter(author__username__icontains=queryagr)
		return render(request,'Agriculture/agsearch.html',{'allpostsuseragr':allpostsuseragr})

def searchdev(request):
	if request.method=='GET':
		querydev=request.GET.get('devquerys')
		allpostsuserdev=DVideo.objects.filter(author__username__icontains=querydev)
		return render(request,'Devotional/desearch.html',{'allpostsuserdev':allpostsuserdev})

def searchedu(request):
	if request.method=='GET':
		queryedu=request.GET.get('eduquerys')
		allpoststitleedu=EdVideo.objects.filter(author__username__icontains=queryedu)
		return render(request,'Education/edsearch.html',{'allpoststitleedu':allpoststitleedu})

def searchexe(request):
	if request.method=='GET':
		queryexe=request.GET.get('exequerys')
		allpoststitleexe=ExVideo.objects.filter(author__username__icontains=queryexe)
		return render(request,'Exercises/exsearch.html',{'allpoststitleexe':allpoststitleexe})


def searchhea(request):
	if request.method=='GET':
		queryhea=request.GET.get('heaquerys')
		allpoststitlehea=HVideo.objects.filter(author__username__icontains=queryhea)
		return render(request,'Health/hesearch.html',{'allpoststitlehea':allpoststitlehea})


def searchoth(request):
	if request.method=='GET':
		queryoth=request.GET.get('othquerys')
		allpoststitleoth=OVideo.objects.filter(author__username__icontains=queryoth)
		return render(request,'Others/otsearch.html',{'allpoststitleoth':allpoststitleoth})


def searchspo(request):
	if request.method=='GET':
		queryspo=request.GET.get('spoquerys')
		allpoststitlespo=SVideo.objects.filter(author__username__icontains=queryspo)
		return render(request,'Sports/spsearch.html',{'allpoststitlespo':allpoststitlespo})


def searchtou(request):
	if request.method=='GET':
		querytou=request.GET.get('touquerys')
		allpoststitletou=TVideo.objects.filter(author__username__icontains=querytou)
		return render(request,'Tourism/tosearch.html',{'allpoststitletou':allpoststitletou})












def followu(request,id):
	userid=id
	#following=get_object_or_404(Profile,id=pk)
	followings=Profile.objects.get(user__id=request.user.id)
	if followings.following.filter(id=userid).exists():
		followings.following.remove(userid)
	else:
		followings.following.add(userid)

	return HttpResponseRedirect(reverse('followposts'))





def post_of_following_profiles(request):
	print(request.user.username)
	profile=Profile.objects.get(user=request.user)
	users=[user for user in profile.following.all()]
	print(users)
	agposts=[]
	spposts=[]
	exposts=[]
	enposts=[]
	otposts=[]
	edposts=[]
	hposts=[]
	dposts=[]
	tposts=[]
	agqs=None
	spqs=None
	exqs=None
	edqs=None
	enqs=None
	hqs=None
	dqs=None
	tqs=None
	oqs=None
	for u in users:
		p_agriculture=AgPost.objects.filter(author=u)
		p_sports=SPost.objects.filter(author=u)
		p_exercises=ExPost.objects.filter(author=u)
		p_education=EdPost.objects.filter(author=u)
		p_entertainment=EnPost.objects.filter(author=u)
		p_health=HPost.objects.filter(author=u)
		p_devotinal=DPost.objects.filter(author=u)
		p_tourism=TPost.objects.filter(author=u)
		p_other=OPost.objects.filter(author=u)
		agposts.append(p_agriculture)
		spposts.append(p_sports)
		exposts.append(p_exercises)
		enposts.append(p_entertainment)
		otposts.append(p_other)
		edposts.append(p_education)
		hposts.append(p_health)
		dposts.append(p_devotinal)
		tposts.append(p_tourism)
		if len(agposts)>0:
			agqs=sorted(chain(*agposts),reverse=True ,key=lambda obj:obj.date)
		if len(spposts)>0:
			spqs=sorted(chain(*spposts),reverse=True ,key=lambda obj:obj.date)
		if len(exposts)>0:
			exqs=sorted(chain(*exposts),reverse=True ,key=lambda obj:obj.date)
		if len(edposts)>0:
			edqs=sorted(chain(*edposts),reverse=True ,key=lambda obj:obj.date)
		if len(enposts)>0:
			enqs=sorted(chain(*enposts),reverse=True ,key=lambda obj:obj.date)
		if len(hposts)>0:
			hqs=sorted(chain(*hposts),reverse=True ,key=lambda obj:obj.date)
		if len(dposts)>0:
			dqs=sorted(chain(*dposts),reverse=True ,key=lambda obj:obj.date)
		if len(tposts)>0:
			tqs=sorted(chain(*tposts),reverse=True ,key=lambda obj:obj.date)
		if len(otposts)>0:
			oqs=sorted(chain(*otposts),reverse=True ,key=lambda obj:obj.date)
	return render(request,'following.html',{'agposts':agqs,'spposts':spqs,'exposts':exqs,'edposts':edqs,'enposts':enqs,'hposts':hqs,'dposts':dqs,'tposts':tqs,'oposts':oqs})
