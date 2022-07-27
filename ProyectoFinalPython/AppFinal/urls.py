from xml.etree.ElementInclude import include
from django.urls import path
from AppFinal.views import index, nosotros, reseñas, LogInClient, SignUpClient, UpdateClient, LogOutClient, ProfileClient, dummy



urlpatterns = [
    path('',index),
    path('index/', index, name = "Index"),
    path ('nosotros/', nosotros),
    path ('reseñas/', reseñas),
    path ("Iniciar-sesion/", LogInClient.as_view(), name = "IniciarSesion"),
    path ("Registrarse/", SignUpClient.as_view(), name = "Registrarse"),
    path ("actualizar/<pk>", UpdateClient.as_view(), name = "Actualizar"),
    path ("Cerrar-Sesion/", LogOutClient.as_view(), name= "CerrarSesion"),
    path ('dummy', dummy, name= "dummy"),
    path ("perfil/<pk>", ProfileClient.as_view(), name= "Perfil"),

   
]