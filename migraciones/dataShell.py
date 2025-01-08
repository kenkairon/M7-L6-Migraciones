import os
import django
from datetime import date

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'migraciones.settings')
django.setup()

# Importar los modelos
from modelos.models import Autor, Libro

def poblar_datos():
    # Crear autores
    autor1 = Autor.objects.create(nombre="Jane Austen", correo="jane.austen@example.com")
    autor2 = Autor.objects.create(nombre="George Orwell", correo="george.orwell@example.com")

    # Crear libros
    Libro.objects.create(titulo="Orgullo y prejuicio", fecha_publicacion=date(1813, 1, 28), autor=autor1)
    Libro.objects.create(titulo="1984", fecha_publicacion=date(1949, 6, 8), autor=autor2)
    Libro.objects.create(titulo="Emma", fecha_publicacion=date(1815, 12, 23), autor=autor1)

    print("Datos iniciales cargados con éxito.")

if __name__ == "__main__":
    poblar_datos()
