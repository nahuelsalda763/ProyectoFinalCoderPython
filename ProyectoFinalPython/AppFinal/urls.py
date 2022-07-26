from xml.etree.ElementInclude import include
from django.urls import path
from AppFinal.views import index, nosotros, reseñas
from AppFinal import views
from ProyectoFinalPython.AppFinal.views import SignUpClient, lo
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',index),
    path('index/', index),
    path ('nosotros/', nosotros),
    path ('reseñas/', reseñas),
    path ("Iniciar-sesion/", views.LogInClient.as_view(), name = "IniciarSesion"),
    path ("Registrarse/", views.SignUpClient.as_view(), name = "Registrarse"),
    path ("perfil/", views.UpdateClient.as_view(), name = "perfil"),

   
]