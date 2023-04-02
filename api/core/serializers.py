from rest_framework import serializers
from .models import Cliente, Funcionario

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'endereco', 'idade']

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'endereco', 'idade', 'salario']