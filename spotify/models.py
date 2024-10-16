from django.db import models

class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)  # Campo para la biografía del artista
    fecha_nacimiento = models.DateField(null=True, blank=True)  # Campo para la fecha de nacimiento

    def __str__(self):
        return self.nombre


class Album(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    fecha_lanzamiento = models.DateField()
    genero = models.CharField(max_length=50)  # Permite cualquier género

    def __str__(self):
        return f"{self.titulo} de {self.artista.nombre}"


class Cancion(models.Model):
    titulo = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duracion = models.DurationField()  # Duración de la canción

    def __str__(self):
        return f"{self.titulo} de {self.album.titulo}"


class Playlist(models.Model):
    nombre = models.CharField(max_length=100)
    canciones = models.ManyToManyField(Cancion)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
