from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from myapp.views import OsobaViewSet, StanowiskoViewSet

from . import views

router = DefaultRouter()
router.register(r'osoba', OsobaViewSet)  
router.register(r'stanowisko', StanowiskoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("team/<int:id>", views.team_detail),
    path("teams", views.team_list),
    path("person/<int:id>", views.person_detail),
    path("persons", views.person_list),
    path("welcome", views.welcome_view),
    path('admin/', admin.site.urls),
]
