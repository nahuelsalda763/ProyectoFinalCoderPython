
from http import client
from AppFinal.models import Client, Product, Comment
from AppFinal.forms import Comment_form, BusquedaProductos, Client_Form
from django.shortcuts import get_object_or_404, render
from django.http import  HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DetailView, ListView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

def index(request):
    productos = Product.objects.filter(SKU=357)
    return render(request, 'AppFinal/index.html', {"productos":productos})

def nosotros(request):
    return render(request, "AppFinal/nosotros.html", {})

def Reseñas(request):
    comentarios = Comment.objects.all()
    if request.method == 'GET':
        form = Comment_form()
        context = {'form':form,'comentarios':comentarios}
    else:
        form = Comment_form(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            nuevo_descripcion = Comment ( comments = data["comments"], punctuation = data["punctuation"], name = data["name"])
            nuevo_descripcion.save()
            context = {'comentarios':comentarios}
    
    return render(request, 'AppFinal/reseñas.html', context=context)


class CreateProduct(LoginRequiredMixin, CreateView):

    model = Product
    success_url = reverse_lazy("Productos")
    fields = ["name", "price", "desc", "SKU", "stock", "image"]


class UpdateProduct(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'AppFinal/actualizarProducto.html'
    fields = ["name", "price", "desc","SKU","stock","image"]
    success_url = reverse_lazy("Productos")

class DeleteProduct(LoginRequiredMixin,DeleteView):
    model = Product
    template_name ='AppFinal/eliminarProducto.html'
    success_url = reverse_lazy("Productos")

class ListViewProducts(ListView):
    model = Product
    template_name = 'AppFinal/productos.html'

class DetailViewProducts(DetailView):
    model = Product
    template_name = 'AppFinal/detalleproductos.html'


def confirmacioncompra(request):
    return render(request, "AppFinal/compra.html", {})
    
def comprafallida(request):
    return render(request, "AppFinal/comprafallida.html", {})

def busqueda_productos(request):
    busqueda_formulario = BusquedaProductos()

    if request.GET:
        resultado = Product.objects.filter(name__icontains = request.GET["search"]).all()

    else:
        resultado = []
    
    return render(request, "AppFinal/busqueda.html", {"busqueda_formulario": busqueda_formulario, "resultado": resultado})

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


@login_required
def addWishlist(request, id):
    product = get_object_or_404(Product, id=id) # Capturar el ID del producto
    if product.users_wishlist.filter(id=request.user.id).exists(): #busca el item e intenta matchearlo con el id del usuario, si esto concuerda es pq el cliente ya añadio ese producto a la wishlist
            product.users_wishlist.remove(request.user)
            messages.success(request, product.name + " has been removed from your WishList")
    else:
        product.users_wishlist.add(request.user) #add the data to the db
        messages.success(request, "Added " + product.name + " to your WishList")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])# redirijos a donde provieneb

@login_required
def wishlist(request):
    #collect data from the db about wishlist and user
    #donde el user agrego el product al wishlist, ver en la tabla del procucto donde matchea con el user
    products = Product.objects.filter(users_wishlist = request.user)
    return render(request, 'AppFinal/user_wishlist.html', {"wishlist" : products})