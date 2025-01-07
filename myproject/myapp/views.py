from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Osoba, Stanowisko, Person, Team
from .serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.filters import SearchFilter

from django.http import Http404, HttpResponse

import datetime

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

def person_list(request):
    persons = Person.objects.all()
    return render(request,
                  "myapp/person/list.html",
                  {'persons': persons})

def person_detail(request, id):
    try:
        person = Person.objects.get(id=id)
    except Person.DoesNotExist:
        raise Http404("Obiekt Person o podanym id nie istnieje")

    return render(request,
                  "myapp/person/detail.html",
                  {'person': person})

def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)

def team_list(request):
    teams = Team.objects.all()
    
    return render(request,
                  "myapp/team/list.html",
                  {'teams': teams})

def team_detail(request, id):
    try:
        team = Team.objects.get(id=id)
    except Team.DoesNotExist:
        raise Http404("Obiekt Team o podanym id nie istnieje")

    return render(request,
                  "myapp/team/detail.html",
                  {'team': team})