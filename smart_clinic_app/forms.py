from django import forms
from django.contrib.auth.models import User , Group
from django.db.models import fields
from django.forms import widgets
from . import models 

class Userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email']

widgets = { 

    'First name' : forms.TextInput(attrs={'class':'form-field'}),
    'Last name' : forms.TextInput(attrs={'class' : 'form-field'}),
    'Username' : forms.TextInput(attrs={'class' : 'form-field'}),
    'Email' : forms.TextInput(attrs={'class' : 'form-field'}),
}
class Userforma(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username']

widgets = { 

    'First name' : forms.TextInput(attrs={'class':'form-field'}),
    'Last name' : forms.TextInput(attrs={'class' : 'form-field'}),
    'Username' : forms.TextInput(attrs={'class' : 'form-field'}),
}