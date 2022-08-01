from AppFinal.models import Product, Comentarios
from django import forms

class Product_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class Comentarios_form(forms.ModelForm):
    # comentario = forms.CharField(widget=forms.Textarea(attrs={
    #     'class': 'md-textarea form-control',
    #     'placeholder': 'Deja tu comentario...',
    #     'rows': '4',
    # }))
    class Meta:
        model = Comentarios
        fields = ['comentario','puntuacion']

class Busqueda_form(forms.Form):
    producto = forms.CharField()
