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
