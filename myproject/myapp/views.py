from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Osoba, Stanowisko, Person, Team
from .serializers import OsobaSerializer, StanowiskoSerializer
from rest_framework.filters import SearchFilter
from django.http import Http404, HttpResponse, JsonResponse
import datetime
from .permissions import IsOwner
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied

def person_view(request, pk):
    try:
        person = Osoba.objects.get(pk=pk)
        
        if request.user == person.wlasciciel:
            return HttpResponse(f"Ten użytkownik nazywa się {person.imie} {person.nazwisko}")
        
        if not request.user.has_perm('ankiety.can_view_other_persons'):
            raise PermissionDenied("Nie masz uprawnień do wyświetlenia tej osoby.")
        
        return HttpResponse(f"Ten użytkownik nazywa się {person.imie} {person.nazwisko}")
    
    except Osoba.DoesNotExist:
        return HttpResponse(f"W bazie nie ma użytkownika o id={pk}.")

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def stanowisko_members(request, id):
    """
    Wyświetla wszystkie osoby przypisane do danego stanowiska.
    """
    stanowisko = get_object_or_404(Stanowisko, id=id)
    members = Osoba.objects.filter(stanowisko=stanowisko)  # Filtruj osoby po stanowisku

    members_list = [
        {"id": member.id, "name": member.name, "age": member.age}
        for member in members
    ]

    return JsonResponse({
        "stanowisko": stanowisko.name,
        "members": members_list
    })

@api_view(['PUT'])
def person_update(request, id):
    """
    Aktualizacja osoby.
    """
    person = get_object_or_404(Osoba, id=id)
    data = request.data

    person.name = data.get('name', person.name)
    person.age = data.get('age', person.age)
    person.save()

    return JsonResponse({
        "message": "Person updated successfully",
        "person": {
            "id": person.id,
            "name": person.name,
            "age": person.age,
        }
    })

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def person_delete(request, id):
    """
    Usuwanie osoby - wymaga uwierzytelnienia przez token.
    """
    person = get_object_or_404(Osoba, id=id)
    person.delete()

    return JsonResponse({"message": "Person deleted successfully"})


class OsobaViewSet(viewsets.ModelViewSet):
    queryset = Osoba.objects.all()
    serializer_class = OsobaSerializer
    permission_classes = [IsOwner]
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
    if request.user.is_authenticated:
        persons = Osoba.objects.filter(wlasciciel=request.user)
    else:
        persons = Osoba.objects.none()
    
    return render(request, "myapp/person/list.html", {'persons': persons})

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