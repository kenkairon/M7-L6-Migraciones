# M7-L6-Migraciones
Educativo y de Aprendizaje Personal

---
## Tabla de Contenidos
- [Tecnologías](#Tecnologías)
- [Configuración Inicial](#configuración-Inicial)
- [Creación del Modelo](#creación-del-modelo)
---
# Tecnologías
- Django: Framework web en Python.
- SQLite:
--- 
# Configuración Inicial 
1. Entorno virtual 
    ```bash 
    python -m venv venv

2. Activar el entorno virtual
    ```bash 
    venv\Scripts\activate

3. Instalar Django
    ```bash 
    pip install django 
        
4. Actualizamos el pip 
    ```bash
    python.exe -m pip install --upgrade pip

5. Crear el proyecto de django migraciones
    ```bash 
    django-admin startproject migraciones

6. Guardamos dependencias
    ```bash
    pip freeze > requirements.txt

7. Ingresamos al proyecto 
    ```bash 
    cd migraciones

9. Creamos la aplicacion llamada modelos
    ```bash     
    python manage.py startapp modelos


10. Configuración de crud/settings.py 
    ```bash 
        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'modelos',
        ]
       



# Creación del Modelo 

11. en app1/models.py
    ```bash
    from django.db import models

    # Create your models here.
    class Autor(models.Model):
        nombre = models.CharField(max_length=100)
        correo = models.EmailField()
        
        def __str__(self):
            return self.nombre

    class Libro(models.Model):
        titulo = models.CharField(max_length=200)
        fecha_publicacion = models.DateField()
        autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
        
        def __str__(self):
            return self.titulo

12. Hacemos las migraciones correspondientes
    ```bash
    python manage.py makemigrations
    python manage.py migrate

13. modelos/views.py
    ```bash
    from django.shortcuts import render
    from .models import Autor, Libro
    # Create your views here.

    from django.shortcuts import render
    from .models import Autor, Libro

    def index(request):
        autores = Autor.objects.all()
        libros = Libro.objects.all()
        context = {
            'autores': autores,
            'libros': libros
        }
        print(context['autores'][0].correo)
        print(context['autores'][1])
        print(context['libros'][0])
        print(context['libros'][1])
        print(context['libros'][2])
        return render(request, 'modelos/index.html', context)


14. en migraciones/urls.py
    ```bash
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('modelos.urls')),
    ]

15. modelos/urls.py
    ```bash
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
16. Nos Vamos http://127.0.0.1:8000/ 
    ```bash
    python manage.py runserver