from django.urls import path
from AppFinal.views import index, nosotros, Reseñas, ListViewProducts, DetailViewProducts, LogInClient, SignUpClient, UpdateClient, LogOutClient, ProfileClient, dummy, busqueda_productos, confirmacioncompra,comprafallida, addWishlist, wishlist, CreateProduct, DeleteProduct, UpdateProduct
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path ('',index),
    path ('index/', index, name = "Index"),
    path ('nosotros/', nosotros, name= "Nosotros"),
    path ('reseñas/', Reseñas, name = "Reseñas"),
    path ('productos/', ListViewProducts.as_view(), name = "Productos"),
    path ('detalleproductos/<int:pk>/', DetailViewProducts.as_view(), name="DetalleProductos" ),
    path ('nuevoProducto/', CreateProduct.as_view(), name = "NuevoProducto"),
    path ('eliminarProducto/<int:pk>/', DeleteProduct.as_view(), name = "EliminarProducto"),
    path ('actualizarProducto/<int:pk>/', UpdateProduct.as_view(), name = "ActualizarProducto"),
    path ('busqueda/',  busqueda_productos , name="Busqueda"),
    path ('compra/', confirmacioncompra),
    path ('comprafallida/', comprafallida),
    path ("Iniciar-sesion/", LogInClient.as_view(), name = "IniciarSesion"),
    path ("Registrarse/", SignUpClient.as_view(), name = "Registrarse"),
    path ("actualizar/<int:pk>/", UpdateClient.as_view(), name = "Actualizar"),
    path ("Cerrar-Sesion/", LogOutClient.as_view(), name= "CerrarSesion"),
    path ("perfil/<int:pk>/", ProfileClient.as_view(), name= "Perfil"),
    path ('dummy', dummy, name= "dummy"),
    path ("addWishlist/<int:id>/", addWishlist, name = "user_wishlist"),
    path ("wishlist/", wishlist, name = "WishList")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)