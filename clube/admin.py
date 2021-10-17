from django.contrib import admin
from clube.models import Storie, Clube, Usuario, UsuarioClube


class Usuarios(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password')
    list_display_links = ('username', 'email', 'password')
    search_fields = ('username', 'email')
    list_per_page = 20
    ordering = ('email',)


admin.site.register(Usuario, Usuarios)


class Clubes(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao')
    list_display_links = ('nome', 'descricao')
    search_fields = ('nome', 'descricao')
    list_per_page = 20


admin.site.register(Clube, Clubes)


class Stories(admin.ModelAdmin):
    list_display = ('id', 'clube', 'usuario', 'data', 'texto')
    list_display_links = ('id', 'data', 'texto')
    search_fields = ('clube', 'usuario')
    list_per_page = 20


admin.site.register(Storie, Stories)


class UsuarioClubes(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'clube', 'ativo')
    list_display_links = ('id', 'clube', 'usuario', 'ativo')
    search_fields = ('clube', 'usuario')
    list_per_page = 20


admin.site.register(UsuarioClube, UsuarioClubes)
