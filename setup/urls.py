from django.contrib import admin
from django.urls import path, include
from clube.views import ListaClubesUsuario, ListaStoriesClube, UsuarioViewSet, ClubesViewSet, StorieViewSet, UsuarioClubeViewSet
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


router = routers.DefaultRouter()
router.register('usuarios', UsuarioViewSet, basename='Usuarios')
router.register('clubes', ClubesViewSet, basename='Clubes')
router.register('stories', StorieViewSet, basename='Stories')
router.register('usuarioClubes', UsuarioClubeViewSet, basename='UsuarioClubes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('usuario/<int:pk>/clubes/', ListaClubesUsuario.as_view()),
    path('clube/<int:pk>/stories/', ListaStoriesClube.as_view()),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]