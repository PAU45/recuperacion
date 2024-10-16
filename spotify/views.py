from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Artista, Album, Cancion, Playlist
from .serializers import ArtistaSerializer, AlbumSerializer, CancionSerializer, PlaylistSerializer

# Vistas para Artista
class ArtistaListaVista(APIView):
    
    def get(self, request):
        artistas = Artista.objects.all()
        serializer = ArtistaSerializer(artistas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArtistaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArtistaDetalleVista(APIView):
    
    def get(self, request, pk):
        artista = get_object_or_404(Artista, pk=pk)
        serializer = ArtistaSerializer(artista)
        return Response(serializer.data)

    def put(self, request, pk):
        artista = get_object_or_404(Artista, pk=pk)
        serializer = ArtistaSerializer(artista, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        artista = get_object_or_404(Artista, pk=pk)
        artista.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Vistas para Playlist
class PlaylistListaVista(APIView):
    
    def get(self, request):
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlaylistSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PlaylistDetalleVista(APIView):
    
    def get(self, request, pk):
        playlist = get_object_or_404(Playlist, pk=pk)
        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data)

    def put(self, request, pk):
        playlist = get_object_or_404(Playlist, pk=pk)
        serializer = PlaylistSerializer(playlist, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        playlist = get_object_or_404(Playlist, pk=pk)
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Vistas para Canción
class CancionListaVista(APIView):
    
    def get(self, request):
        canciones = Cancion.objects.all()
        serializer = CancionSerializer(canciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CancionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CancionDetalleVista(APIView):
    
    def get(self, request, pk):
        cancion = get_object_or_404(Cancion, pk=pk)
        serializer = CancionSerializer(cancion)
        return Response(serializer.data)

    def put(self, request, pk):
        cancion = get_object_or_404(Cancion, pk=pk)
        serializer = CancionSerializer(cancion, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        cancion = get_object_or_404(Cancion, pk=pk)
        cancion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Vistas para Álbum
class AlbumListaVista(APIView):
    
    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AlbumDetalleVista(APIView):
    
    def get(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        serializer = AlbumSerializer(album)
        return Response(serializer.data)

    def put(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        serializer = AlbumSerializer(album, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        album = get_object_or_404(Album, pk=pk)
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
