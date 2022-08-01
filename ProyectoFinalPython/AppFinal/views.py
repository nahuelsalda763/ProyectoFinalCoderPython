from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppFinal.models import Product, Comentarios
from AppFinal.forms import Product_form, Comentarios_form, Busqueda_form
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView, ListView
from django.urls import reverse_lazy, reverse
from django.http import Http404
from django.contrib.auth.views import LoginView, LogoutView

def index(request):
    return render(request, "AppFinal/index.html", {})

def nosotros(request):
    return render(request, "AppFinal/nosotros.html", {})

def reseñas(request):
    return render(request, "AppFinal/reseñas.html", {})

def productos(request):
    return render(request,"AppFinal/productos.html", {})

def iniciarsesion(request):
    return render(request, "AppFinal/iniciarsesion.html", {})

def cerrarsesion(request):
    return render(request, "AppFinal/cerrarsesion.html", {})

def registrarse(request):
    return render(request, "AppFinal/registrarse.html", {})

def busqueda(request):
    return render(request, "AppFinal/busqueda.html", {})

def detalleproductoss(request):
    return render(request, "AppFinal/detalleproductos.html", {})

def confirmacioncompra(request):
    return render(request, "AppFinal/compra.html", {})



class detalleproductos(DetailView):

    model = Product
    template_name = "AppFinal/detalleproductos.html"


class ProductManage(ListView):
    model = Product
    template_name_suffix = 'AppFinal/index.html'

class ProductCreate(CreateView):
    model = Product
    form_class = Product_form
    success_url = reverse_lazy('producto:manage')

class ProductUpdate(UpdateView):
    model = Product
    form_class = Product_form
    template_name_suffix = '_update_form'

    def test_func(self):
        exist = Product.objects.filter(id=self.kwargs['pk'])
        return True if exist else False
    
class ProductoDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('producto:manage')





class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("blog_list")


class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'


def index(request):
    # comentarios = Comentarios.objects.all()
    productos = Product.objects.filter(SKU=357)
    return render(request, 'AppFinal/index.html', {"productos":productos}) 
    # if request.method == 'GET':
    #     form = Comentarios_form()
    #     context = {'form':form,'descripcion':comentarios,'productos':productos}
    #     return render(request, 'AppFinal/index.html', context=context)
    # else:
    #  if request.user.is_authenticated: 
    #     form = Comentarios_form(request.POST)
    #     if form.is_valid():
    #         nuevo_descripcion = Comentarios.objects.create(
    #             comentario = form.cleaned_data['comentario'],
    #             puntuacion = form.cleaned_data['puntuacion'],
    #             usuario = request.user,
    #             imagen = request.user.usuario_perfil.imagen.url,
    #         )
    #         context ={'descripcion':comentarios,'productos':productos}
    #     return redirect('/#comentarios')
    #  else:
    #     context ={'errors':'Debes estar logeado para dejar un comentario'}
    #     return render(request, 'AppFinal/index.html', context=context)
    

    
def TodosLosProductos(request):
    # comentarios = Comentarios.objects.all()
    productos = Product.objects.all()
    context = {"productos": productos}
    return render(request, 'AppFinal/productos.html', context = context) 


def Busqueda_formu(request):
    busqueda_formulario = Busqueda_form()

    if request.GET:
        resultado = Product.objects.filter(name__icontains = request.GET["producto"]).all()

    else:
        resultado = []
    
    return render(request, "AppFinal/busqueda.html", {"busqueda_formulario": busqueda_formulario, "resultado": resultado})



def Reseñas(request):
    comentarios = Comentarios.objects.all()
    if request.method == 'GET':
        form = Comentarios_form()
        context = {'form':form,'descripcion':comentarios,'productos':productos}
        return render(request, 'AppFinal/reseñas.html', context=context)
    else:
     if request.user.is_authenticated: 
        form = Comentarios_form(request.GET)
        if form.is_valid():
            nuevo_descripcion = Comentarios.objects.create(
                comentario = form.cleaned_data['Dejanos tu reseña!'],
                puntuacion = form.cleaned_data['tu puntuacion sobre nuestro proyecto?'],
                usuario = request.user,
                imagen = request.user.usuario_perfil.imagen.url,
            )
            context ={'descripcion':comentarios,'productos':productos}
        return redirect('AppFinal/reseñas.html')
     else:
        context ={'errors':'Debes estar logeado para dejar un comentario'}
        return render(request, 'AppFinal/reseñas.html', context=context)