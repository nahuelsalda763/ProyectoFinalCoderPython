from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, Loginview, UpdateView, SuccessMessageMixin
from AppFinal.models import Client
from django.contrib.auth.models import User


def index(request):
    return render(request, "AppFinal/index.html", {})

def nosotros(request):
    return render(request, "AppFinal/nosotros.html", {})

def reseñas(request):
    return render(request, "AppFinal/reseñas.html", {})

# Clientes

# Crear Cliente
class SignUpClient(CreateView,SuccessMessageMixin): #SuccessMessageMixin: Permite comunicarle al usuario que todo esta OK
    model = User
    template_name = 'Registrarse'
    success_url = reverse_lazy("Iniciaresion") # Luego de haber logrado exitosamente la creacion te redirecciona a ... la url
    form_class = UserCreationForm #Viene con django el form que se usa para crear un user, en este caso un cliente
class LogInClient(Loginview):
    template_name = 'iniciarsesion'
class UpdateClient(UpdateView,LoginRequiredMixin):
    model = User
    template_name = 'perfil'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("perfil", kwargs={"pk": self.request.user.id})

