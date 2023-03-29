from rest_framework import viewset
from serializer import JogoSerializer, LojaSerializer
from .model import Jogo, Loja

class JogoViewSet(viewset.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class LojaViewSet(viewset.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer