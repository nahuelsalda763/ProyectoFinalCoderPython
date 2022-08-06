https://youtu.be/XJH_pPak60E



# PyCommerce

En este proyecto, nuestro equipo busca la mejor forma de representar como seria un eCommerce, en forma de kiosco, ambientado en CoderHouse.
Dentro de el, podras hacer lo siguiente:

- Crear, editar y borrar articulos en venta.
- Seleccionar articulos y dejarlos en un carrito hasta ser comprados.
- Crearte un usuario para tener tu propio carrito de compras.
- Dejar una reseña de tu opinion sobre el servicio 

(Aclaracion: Los productos destacados/del dia son los que tengan SKU: 357 . Esto lo realizamos bajo el criterio de que no siempre los productos destacados son los mas visitados o vendidos como te quieren hacer creer, sino que es lo que ellos quieren que veas.)

# Instalacion 

Podras instalar el Software necesario de la siguiente manera:

## Verificar la version de Python
Este proyecto fue escrito con Python 3.9.12, en base a eso sugerimos que lo pruebe con esta version o superior. Todo esto para evitar posibles incompatibilidades.

Como puedo confirmar mi version de Python? 

` El comando de python puede variar segun el sistema operativo, por favor tener eso en cuenta. `

Mac os:

```bash
> python --version
> Python 3.9.12
```

in windows:

```bash
c:\> python3 --version
c:\> Python 3.9.12
```

## Instalar dependencias

Para instalar dependencias, necesitas ejecutar `pip install`, asegurate de estar dentro de la carpeta del archivo y poder visualizar el archivo `requirements.txt` cuando ejecutes `ls` o en su defecto `dir`

```bash
> pip install -r requirements.txt
```
Veras en la terminal como se iran instalando los softwares requeridos.

`Algunos sistemas operativos pueden requerir que utilices pip3 en lugar de pip `

## Configuracion de Django

Una vez terminada la instalacion de las dependencias, deberas de ejecutar unos comandos de Django.

### Migraciones

Crear la base de datos
Mac os:
```bash
> python3 mananage.py migrate
```
windows:
```bash
c:\> python mananage.py migrate
```

### Crear Superuser
Mac os:
```bash
> python3 mananage.py createsuperuser
(Pedira usuario email y contraseña)
```
windows:
```bash
c:\> python mananage.py createsuperuser
(Pedira usuario email y contraseña)
```

### Ejecutar el servidor
Mac os
```bash
> python3 mananage.py runserver
```
windows:
```bash
c:\> python mananage.py runserver
```
