from django.db import models
import sys

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(blank=False, max_length=100, unique=True)
    senha = models.CharField(max_length=30)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Clube (models.Model):
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
    texto = models.CharField(max_length=sys.maxsize)
    
    def __str__(self):
        return self.texto

class UsuarioClube(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)    
    clube = models.ForeignKey(Clube, on_delete=models.CASCADE)   
    ativo = models.BooleanField(default=True)
