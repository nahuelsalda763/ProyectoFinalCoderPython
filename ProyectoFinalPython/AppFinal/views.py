from dataclasses import fields
from string import punctuation
from unicodedata import name

from requests import request
from AppFinal.models import Client, Product, Coments
from AppFinal.forms import Coments_form, BusquedaProductos, Client_Form
from django.shortcuts import get_object_or_404, render
from django.http import  HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "AppFinal/index.html", {})

def nosotros(request):
    return render(request, "AppFinal/nosotros.html", {})

# Clientes

@login_required
def dummy(request):
    render(request, "")

# Registrarse

class SignUpClient(CreateView,SuccessMessageMixin): #SuccessMessageMixin: Permite comunicarle al usuario que todo esta OK
    model = Client
    template_name = 'AppFinal/Registrarse.html'
    success_url = reverse_lazy("IniciarSesion") # Luego de haber logrado exitosamente la creacion te redirecciona a ... la url
    form_class = Client_Form #Viene con django el form que se usa para crear un user, en este caso un cliente

# Inciar Sesion

class LogInClient(LoginView):
    #signals=cuando suceda algo tiene que desencadenar otra accion
    template_name = 'AppFinal/iniciarsesion.html'
    def get_success_url(self):

        return reverse_lazy("Perfil", kwargs={"pk": self.request.user.client.id})
    

# Actualizar datos 

class UpdateClient(UpdateView,LoginRequiredMixin,UserPassesTestMixin): #LoginRequiredMixin: Chequea si el usuario esta loggeado, si no lo esta lo redirecciona a otra pagina(se puede configurar, en general es inicio o error 404)
    # UserPassesTestMixin: chequea que el formato del nuevo dato ingresado sea el adecuando, por ej. en mail el @......com
    model = User
    template_name = 'AppFinal/actualizar.html'
    fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def test_func(self):
        return self.request.user.client.id == int(self.kwargs['pk'])

    def get_success_url(self):
        return reverse_lazy("Perfil", kwargs={"pk": self.request.user.client.id})

   

# Cerrar Sesion

class LogOutClient(LogoutView):
    template_name = "AppFinal/cerrarsesion.html"

# Vista del perfil

class ProfileClient(LoginRequiredMixin,UserPassesTestMixin, DetailView):

    model = Client
    template_name = "AppFinal/perfil.html"

    def test_func(self):
        return self.request.user.client.id == int(self.kwargs['pk'])


# Productos

class ProductManage(ListView):
    model = Product
    template_name = "AppFinal/productos.html"


class DetailView(DetailView):
    model = Product
    template_name = 'detalle_productos'

"""class ComentManage(ListView):
    model = Coments
    template_name_suffix = 'AppFinal/reseñas.html'

    def reseñas(request):
        comentarios = Coments.objects.all()
        if request.method == 'GET':
            form = Coments_form()
            context = {'form':form,'descripcion':comentarios}
            return render(request, 'AppFinal/reseñas.html', context=context)
        else:
            if request.user.is_authenticated: 
                form = Coments_form(request.POST)
                if form.is_valid():
                    nuevo_descripcion = Coments.objects.create(
                        comentario = form.cleaned_data['coments'],
                        puntuacion = form.cleaned_data['puntuation'],
                        usuario = request.user,
                    )
                    context ={'descripcion':comentarios}
                return redirect('AppFinal/reseñas.html')
            else:
                context ={'errors':'Debes estar logeado para dejar un comentario'}
                return render(request, 'AppFinal/reseñas.html', context=context)


"""
def busqueda_productos(request):
    busqueda_formulario = BusquedaProductos()

    if request.GET:
        productos = Product.objects.filter(name=request.GET["search"]).all()

    else:
        productos = []

    return render(request, "AppFinal/productos.html", {"busqueda_formulario": busqueda_formulario, "productos": productos})

def Reseñas(request):
    comentarios = Coments.objects.all()
    if request.method == 'GET':
        form = Coments_form()
        context = {'form':form,'comentarios':comentarios}
    else:
        form = Coments_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            nuevo_descripcion = Coments ( coments = data["coments"], puntuation = data["puntuation"], name = data["name"])
            nuevo_descripcion.save()
            context = {'comentarios':comentarios}
    
    return render(request, 'AppFinal/reseñas.html', context=context)

@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id) # Capturar el ID del producto
    if product.users_wishlist.filter(id=request.user.client.id).exists(): #busca el item e intenta matchearlo con el id del usuario, si esto concuerda es pq el cliente ya añadio ese producto a la wishlist
            product.users_wishlist.remove(request.user.client)
    else:
        product.users_wishlist.add(request.user) #add the data to the db
    return HttpResponseRedirect(request.META["HTTP_REFERER"])# redirijos a donde provieneb