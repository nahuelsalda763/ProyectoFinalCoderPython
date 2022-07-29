from AppFinal.models import Coments, Client
from django import forms
from django.contrib.auth.models import User  
from django.core.exceptions import ValidationError  
from django.contrib.auth.forms import UserCreationForm  

class Client_Form(UserCreationForm,forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'username','email', 'first_name', 'last_name']

class Coments_form(forms.ModelForm):
    comentario = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Deja tu comentario...',
        'rows': '4',
    }))
    class Meta:
        model = Coments
        fields = ['coments','puntuation']

class BusquedaProductos(forms.Form):
    search = forms.CharField()



   