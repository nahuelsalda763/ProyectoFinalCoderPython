from xml.etree.ElementInclude import include
from django.urls import path
from AppFinal.views import index, nosotros, Reseñas, ProductManage, LogInClient, SignUpClient, UpdateClient, LogOutClient, ProfileClient, dummy, busqueda_productos



urlpatterns = [
    path('',index),
    path('index/', index, name = "Index"),
    path ('nosotros/', nosotros),
    path ('reseñas/', Reseñas, name = "Reseñas"),
    path ('productos/', ProductManage.as_view(), name = "Productos"),
    path ("Iniciar-sesion/", LogInClient.as_view(), name = "IniciarSesion"),
    path ("Registrarse/", SignUpClient.as_view(), name = "Registrarse"),
    path ("actualizar/<int:pk>/", UpdateClient.as_view(), name = "Actualizar"),
    path ("Cerrar-Sesion/", LogOutClient.as_view(), name= "CerrarSesion"),
    path ('dummy', dummy, name= "dummy"),
    path ("perfil/<int:pk>/", ProfileClient.as_view(), name= "Perfil"),
]