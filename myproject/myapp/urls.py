from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from myapp.views import (
    OsobaViewSet, StanowiskoViewSet, 
    team_detail, team_list, 
    person_detail, person_list, 
    welcome_view, stanowisko_members,
    person_update, person_delete,
)
from myapp import views

router = DefaultRouter()
router.register(r"osoba", OsobaViewSet)
router.register(r"stanowisko", StanowiskoViewSet)

urlpatterns = [
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("api-auth/", include("rest_framework.urls")),
    
    path("stanowisko/<int:id>/members/", views.stanowisko_members, name="stanowisko_members"),
    path("person/<int:id>/update", views.person_update, name="person_update"),
    path("person/<int:id>/delete", views.person_delete, name="person_delete"),

    path("teams/", team_list, name="team_list"),
    path("team/<int:id>/", team_detail, name="team_detail"),
    path("persons/", person_list, name="person_list"),
    path("person/<int:id>/", person_detail, name="person_detail"),
    path("welcome/", welcome_view, name="welcome_view"),
    
    path("admin/", admin.site.urls),
    
    path("", include(router.urls)),
]
