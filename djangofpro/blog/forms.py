from django import forms
from .models import ExPost,EdPost,SPost,EnPost,AgPost,EnVideo,ExVideo,EdVideo,SVideo,AgVideo,excomment,edcomment,encomment,spcomment,agcomment,tcomment,hcomment,ocomment,dcomment,HPost,DPost,TPost,OPost,HVideo,TVideo,CoVideo,OVideo,DVideo
class ExForm(forms.ModelForm):
	class Meta:
		model = ExPost
		fields=('title','author','text','header_image')

		widgets={
			'title' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'exercise','type':'hidden'}),
			'text' :forms.Textarea(attrs={'class': 'form-control'}),

		}
class HForm(forms.ModelForm):
	class Meta:
		model = HPost
		fields=('title','author','text','header_image')

		widgets={
			'title' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'health','type':'hidden'}),
			'text' :forms.Textarea(attrs={'class': 'form-control'}),

		}

class TForm(forms.ModelForm):
	class Meta:
		model = TPost
		fields=('title','author','text','header_image')

		widgets={
			'title' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'tourism','type':'hidden'}),
			'text' :forms.Textarea(attrs={'class': 'form-control'}),

		}

class DForm(forms.ModelForm):
	class Meta:
		model = DPost
		fields=('title','author','text','header_image')

		widgets={
			'title' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'devotion','type':'hidden'}),
			'text' :forms.Textarea(attrs={'class': 'form-control'}),

		}

class OForm(forms.ModelForm):
	class Meta:
		model = OPost
		fields=('title','author','text','header_image')

		widgets={
			'title' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'other','type':'hidden'}),
			'text' :forms.Textarea(attrs={'class': 'form-control'}),

		}


class EdForm(forms.ModelForm):
	class Meta:
		model = EdPost
		fields=('title','author','text','header_image')

		widgets={
			'title' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'education','type':'hidden'}),
			'text' :forms.Textarea(attrs={'class': 'form-control'}),
			
		}		



class SForm(forms.ModelForm):
	class Meta:
		model = SPost
		fields=('title','author','text','header_image')

		widgets={
			'title' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'sports','type':'hidden'}),
			'text' :forms.Textarea(attrs={'class': 'form-control'}),
			

		}


class EnForm(forms.ModelForm):
	class Meta:
		model = EnPost
		fields=('title','author','text','header_image')

		widgets={
			'title' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'entertainment','type':'hidden'}),
			'text' :forms.Textarea(attrs={'class': 'form-control'}),
		   

		}


class AgForm(forms.ModelForm):
	class Meta:
		model = AgPost
		fields=('title','author','text','header_image')

		widgets={
			'title' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'agriculture','type':'hidden'}),
			'text' :forms.Textarea(attrs={'class': 'form-control'}),
		  

		}


class EnvForm(forms.ModelForm):
	class Meta:
		model=EnVideo
		fields=("caption","video","text","author")
		widgets={
		    'caption':forms.TextInput(attrs={'class': 'form-control'}),
			'text' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'envdo','type':'hidden'}),

		
}

class HvForm(forms.ModelForm):
	class Meta:
		model=HVideo
		fields=("caption","video","text","author")
		widgets={
		    'caption':forms.TextInput(attrs={'class': 'form-control'}),
			'text' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'hvdo','type':'hidden'}),

		
}

class TvForm(forms.ModelForm):
	class Meta:
		model=TVideo
		fields=("caption","video","text","author")
		widgets={
		    'caption':forms.TextInput(attrs={'class': 'form-control'}),
			'text' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'tvdo','type':'hidden'}),

		
}

class CovForm(forms.ModelForm):
	class Meta:
		model=CoVideo
		fields=("caption","video","text","author")
		widgets={
		    'caption':forms.TextInput(attrs={'class': 'form-control'}),
			'text' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'covdo','type':'hidden'}),

		
}

class DvForm(forms.ModelForm):
	class Meta:
		model=DVideo
		fields=("caption","video","text","author")
		widgets={
		    'caption':forms.TextInput(attrs={'class': 'form-control'}),
			'text' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'dvdo','type':'hidden'}),

		
}

class OvForm(forms.ModelForm):
	class Meta:
		model=OVideo
		fields=("caption","video","text","author")
		widgets={
		    'caption':forms.TextInput(attrs={'class': 'form-control'}),
			'text' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'ovdo','type':'hidden'}),

		
}

class ExvForm(forms.ModelForm):
	class Meta:
		model=ExVideo
		fields=("caption","video","text","author")
		widgets={
		    'caption':forms.TextInput(attrs={'class': 'form-control'}),
			'text' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'exvdo','type':'hidden'}),
		
}

class EdvForm(forms.ModelForm):
	class Meta:
		model=EdVideo
		fields=("caption","video","text",'author')
		widgets={
		    'caption':forms.TextInput(attrs={'class': 'form-control'}),
			'text' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'edvdo','type':'hidden'}),

		
}

class SvForm(forms.ModelForm):
	class Meta:
		model=SVideo
		fields=("caption","video","text",'author')
		widgets={
		    'caption':forms.TextInput(attrs={'class': 'form-control'}),
			'text' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'spvdo','type':'hidden'}),

		
}

class AgvForm(forms.ModelForm):
	class Meta:
		model=AgVideo
		fields=("caption","author","video")

		widgets={
		    'caption':forms.TextInput(attrs={'class': 'form-control'}),
		    'text' :forms.TextInput(attrs={'class': 'form-control'}),
			'author' :forms.TextInput(attrs={'class': 'form-control','value':'','id':'agvdo','type':'hidden'}),

		
}
class ExcmntForm(forms.ModelForm):
	class Meta:
		model = excomment
		fields=('text',)

		widgets={
			'text' :forms.TextInput(attrs={'class': 'form-control'}),

		}

class EdcmntForm(forms.ModelForm):
	class Meta:
		model = edcomment
		fields=('text',)

		widgets={
			'text' :forms.TextInput(attrs={'class': 'form-control'}),

		}

class EncmntForm(forms.ModelForm):
	class Meta:
		model = encomment
		fields=('text',)

		widgets={
			'text' :forms.TextInput(attrs={'class': 'form-control'}),

		}

class SpcmntForm(forms.ModelForm):
	class Meta:
		model = spcomment
		fields=('text',)

		widgets={
			'text' :forms.TextInput(attrs={'class': 'form-control'}),

		}

class AgcmntForm(forms.ModelForm):
	class Meta:
		model = agcomment
		fields=('text',)

		widgets={
			'text' :forms.TextInput(attrs={'class': 'form-control'}),

		}

class tcmntForm(forms.ModelForm):
	class Meta:
		model = tcomment
		fields=('text',)

		widgets={
			'text' :forms.TextInput(attrs={'class': 'form-control'}),

		}

class hcmntForm(forms.ModelForm):
	class Meta:
		model = hcomment
		fields=('text',)

		widgets={
			'text' :forms.TextInput(attrs={'class': 'form-control'}),

		}

class ocmntForm(forms.ModelForm):
	class Meta:
		model = ocomment
		fields=('text',)

		widgets={
			'text' :forms.TextInput(attrs={'class': 'form-control'}),

		}

class dcmntForm(forms.ModelForm):
	class Meta:
		model = dcomment
		fields=('text',)

		widgets={
			'text' :forms.TextInput(attrs={'class': 'form-control'}),

		}














