from django.urls import path
from AppFinal.views import index, nosotros, reseñas, productos, iniciarsesion, cerrarsesion, registrarse
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index),
    path('index/', index),
    path ('nosotros/', nosotros),
    path ('reseñas/', reseñas),
    path ('productos/',productos),
    path('cerrarsesion/', cerrarsesion),
    path ('iniciarsesion/', iniciarsesion),
    path ('registrarse/', registrarse),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)