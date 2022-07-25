from django.urls import path
from AppFinal.views import index, nosotros, reseñas

urlpatterns = [
    path('',index),
    path('index/', index),
    path ('nosotros/', nosotros),
    path ('reseñas/', reseñas)
    
]