from rest_framework import viewsets, generics, filters
from clube.models import Clube, Usuario, Storie, UsuarioClube
from clube.serializer import ClubeSerializer, ListaClubesUsuarioSerializer, ListaStoriesClubeSerializer, \
    UsuarioSerializer, StorieSerializer, UsuarioClubeSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from setup.settings import REST_FRAMEWORK


class UsuarioViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os usuarios"""
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nome', 'id']
    search_fields = ['nome', 'email']


class ClubesViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os clubes"""
    queryset = Clube.objects.all()
    serializer_class = ClubeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['nome', 'id']
    search_fields = ['nome', 'tipo']


class StorieViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os Stories"""
    queryset = Storie.objects.all()
    serializer_class = StorieSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = ['data', 'id']


class UsuarioClubeViewSet(viewsets.ModelViewSet):
    """"Exibindo todos os relacionamentos de clubes e usuarios"""
    queryset = UsuarioClube.objects.all()
    serializer_class = UsuarioClubeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filterset_fields = ['ativo']


class ListaClubesUsuario(generics.ListAPIView):
    """"Exibindo todos os clubes de um usuário"""
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 100000
    }

    def get_queryset(self):
        queryset = UsuarioClube.objects.filter(usuario_id=self.kwargs['pk'])
        return queryset

    pagination_class = 2
    serializer_class = ListaClubesUsuarioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



class ListaStoriesClube(generics.ListAPIView):
    """"Exibindo todos os stories de um clube"""

    def get_queryset(self):
        queryset = Storie.objects.filter(clube_id=self.kwargs['pk'])
        return queryset

    serializer_class = ListaStoriesClubeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
