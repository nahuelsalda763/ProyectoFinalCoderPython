from AppFinal.models import Client
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "AppFinal/index.html", {})

def nosotros(request):
    return render(request, "AppFinal/nosotros.html", {})

def reseñas(request):
    return render(request, "AppFinal/reseñas.html", {})

# Clientes

@login_required
def dummy(request):
    render(request, "")

# Registrarse

class SignUpClient(CreateView,SuccessMessageMixin): #SuccessMessageMixin: Permite comunicarle al usuario que todo esta OK
    model = User
    template_name = 'AppFinal/Registrarse.html'
    success_url = reverse_lazy("IniciarSesion") # Luego de haber logrado exitosamente la creacion te redirecciona a ... la url
    form_class = UserCreationForm #Viene con django el form que se usa para crear un user, en este caso un cliente

# Inciar Sesion

class LogInClient(LoginView):
    template_name = 'AppFinal/iniciarsesion.html'
    success_url = reverse_lazy("Perfil")

# Actualizar datos 

class UpdateClient(UpdateView,LoginRequiredMixin,UserPassesTestMixin): #LoginRequiredMixin: Chequea si el usuario esta loggeado, si no lo esta lo redirecciona a otra pagina(se puede configurar, en general es inicio o error 404)
    # UserPassesTestMixin: chequea que el formato del nuevo dato ingresado sea el adecuando, por ej. en mail el @......com
    model = User
    template_name = 'AppFinal/actualizar.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy("Perfil", kwargs={"pk": self.request.user.id})

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])
# Cerrar Sesion

class LogOutClient(LogoutView):
    template_name = "AppFinal/cerrarsesion.html"

# Vista del perfil

class ProfileClient(LoginRequiredMixin,UserPassesTestMixin, DetailView):

    model = Client
    template_name = "AppFinal/perfil.html"

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])
