from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from django.core.exceptions import NON_FIELD_ERRORS

from clube.models import Clube, Usuario, Storie, UsuarioClube


class ClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clube
        fields = ['id', 'nome', 'descricao', 'tipo']


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def validate_nome(self, nome):
        if not nome.replace(' ', '').isalpha():
            raise serializers.ValidationError("Não é permitido a inclusão de números do nome do usuário.")
        return nome

    def validate_senha(self, senha):
        if len(senha) < 8:
            raise serializers.ValidationError("A senha deve conter 8 ou mais digitos")
        return senha


class StorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storie
        fields = '__all__'


class UsuarioClubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioClube
        fields = '__all__'
        validators = [
                UniqueTogetherValidator(
                    queryset=UsuarioClube.objects.all(),
                    fields=('usuario', 'clube'),
                    message="O usuário já está está neste clube."
                )
            ]


class ListaClubesUsuarioSerializer(serializers.ModelSerializer):
    clube_id = serializers.ReadOnlyField(source='clube.id')
    clube_nome = serializers.ReadOnlyField(source='clube.nome')

    class Meta:
        model = UsuarioClube
        fields = ['id', 'clube_id', 'clube_nome', 'ativo']


class ListaStoriesClubeSerializer(serializers.ModelSerializer):
    usuario_id = serializers.ReadOnlyField(source='usuario.id')
    usuario_nome = serializers.ReadOnlyField(source='usuario.nome')

    class Meta:
        model = Storie
        fields = ['id', 'data', 'texto', 'usuario_id', 'usuario_nome']
