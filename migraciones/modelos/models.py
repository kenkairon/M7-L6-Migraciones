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
    
"""
CREATE TABLE Autor (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(254) NOT NULL UNIQUE
);

-- Crear tabla para el modelo Libro
CREATE TABLE Libro (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    fecha_publicacion DATE NOT NULL,
    autor_id INTEGER NOT NULL,
    FOREIGN KEY (autor_id) REFERENCES Autor(id) ON DELETE CASCADE
);

"""