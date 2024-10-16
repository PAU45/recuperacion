from django.urls import path
from .views import (
    ArtistaListaVista,
    ArtistaDetalleVista,
    AlbumListaVista,
    AlbumDetalleVista,
    CancionListaVista,
    CancionDetalleVista,
    PlaylistListaVista,
    PlaylistDetalleVista
)

urlpatterns = [
    path('artistas/', ArtistaListaVista.as_view(), name='artista-lista-crear'),
    path('artistas/<int:pk>/', ArtistaDetalleVista.as_view(), name='artista-detalle'),
    path('albumes/', AlbumListaVista.as_view(), name='album-lista-crear'),
    path('albumes/<int:pk>/', AlbumDetalleVista.as_view(), name='album-detalle'),
    path('canciones/', CancionListaVista.as_view(), name='cancion-lista-crear'),
    path('canciones/<int:pk>/', CancionDetalleVista.as_view(), name='cancion-detalle'),
    path('playlists/', PlaylistListaVista.as_view(), name='playlist-lista-crear'),
    path('playlists/<int:pk>/', PlaylistDetalleVista.as_view(), name='playlist-detalle'),
]
