from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.filters import SearchFilter

class OsobaViewSet(viewsets.ModelViewSet):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['imie', 'nazwisko']

    @action(detail=True, methods=['delete'])
    def remove(self, request, pk=None):
        osoba = self.get_object()
        osoba.delete()
        return Response({"message": "Osoba została usunięta"})

class StanowiskoViewSet(viewsets.ModelViewSet):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer

    @action(detail=True, methods=['delete'])
    def remove(self, request, pk=None):
        stanowisko = self.get_object()
        stanowisko.delete()
        return Response({"message": "Stanowisko zostało usunięte"})

