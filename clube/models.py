from django.db import models
import sys


from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


class Usuario(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    spouse_name = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.email


class Clube(models.Model):
    TIPO = (
        ('L', 'Livro'),
        ('F', 'Filme'),
        ('J', 'Jogo'),
        ('A', 'Anime')
    )
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=1, choices=TIPO, blank=False, null=False)

    def __str__(self):
        return self.nome


class Storie(models.Model):
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateField()
    texto = models.CharField(max_length=10000)

    def __str__(self):
        return self.texto


class UsuarioClube(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
