
from AppFinal.models import Coments
from django import forms
from django.contrib.auth.models import User  

from django.contrib.auth.forms import UserCreationForm  

class Client_Form(UserCreationForm,forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'username','email', 'first_name', 'last_name']

class Coments_form(forms.ModelForm):
    class Meta:
        model = Coments
        fields = ['coments','puntuation','name']

class BusquedaProductos(forms.Form):
    search = forms.CharField()



   