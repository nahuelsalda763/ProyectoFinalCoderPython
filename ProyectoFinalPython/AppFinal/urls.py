from django.urls import path
from AppFinal.views import index, nosotros, reseñas
from django.conf.urls.static import static

urlpatterns = [
    path('',index),
    path('index/', index),
    path ('nosotros/', nosotros),
    path ('reseñas/', reseñas)
    
]