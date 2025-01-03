from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from myapp.models import Osoba, Stanowisko
from myapp.serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework import viewsets

class OsobaAPIView(APIView):

    def get(self, request, format=None):
        """
        Pobiera listę wszystkich osób.
        """
        osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Tworzy nową osobę na podstawie danych przesłanych w żądaniu.
        """
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        """
        Aktualizuje dane osoby o danym pk.
        """
        try:
            osoba = Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Usuwa osobę o danym pk.
        """
        try:
            osoba = Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OsobaViewSet(viewsets.ModelViewSet):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer

class StanowiskoViewSet(viewsets.ModelViewSet):
    queryset = Stanowisko.objects.all()
    serializer_class = StanowiskoSerializer

