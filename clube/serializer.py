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

    def validate_username(self, username):
        if not username.replace(' ', '').isalpha():
            raise serializers.ValidationError("Não é permitido a inclusão de números do nome do usuário.")
        return username

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError("A senha deve conter 8 ou mais digitos")
        return password


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
    usuario_username = serializers.ReadOnlyField(source='usuario.username')

    class Meta:
        model = Storie
        fields = ['id', 'data', 'texto', 'usuario_id', 'usuario_username']
