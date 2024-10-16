from rest_framework import serializers
from .models import Artista, Album, Cancion, Playlist

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ['id', 'nombre', 'biografia', 'fecha_nacimiento']  # Incluyendo los nuevos campos

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'titulo', 'artista', 'fecha_lanzamiento', 'genero']

class CancionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancion
        fields = ['id', 'titulo', 'album', 'duracion']

class PlaylistSerializer(serializers.ModelSerializer):
    canciones = CancionSerializer(many=True)  # Serializa las canciones de la playlist

    class Meta:
        model = Playlist
        fields = ['id', 'nombre', 'canciones', 'fecha_creacion']
