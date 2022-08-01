from django.urls import path
from AppFinal.views import index, nosotros, Reseñas, productos, confirmacioncompra, detalleproductos, iniciarsesion, cerrarsesion, registrarse, TodosLosProductos, Busqueda_formu
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',index),
    path('index/', index, name="index"),
    path ('nosotros/', nosotros, name="nosotros"),
    path ('reseñas/', Reseñas, name="reseñas"),
    path ('productos/',TodosLosProductos, name="productos"),
    path ('busqueda/', Busqueda_formu , name="busqueda"),
    path('cerrarsesion/', cerrarsesion, name="cerrarsesion"),
    path ('iniciarsesion/', iniciarsesion, name="iniciarsesion"),
    path ('registrarse/', registrarse, name="registrarse"),
    path ('detalleproductos/<int:pk>/', detalleproductos.as_view(), name="productitos" ),
    path ('compra/', confirmacioncompra)
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)