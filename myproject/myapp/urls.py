from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  
from myapp.views import OsobaViewSet, StanowiskoViewSet, team_detail, team_list, person_detail, person_list, welcome_view
from myapp import views

router = DefaultRouter()
router.register(r'osoba', OsobaViewSet)  
router.register(r'stanowisko', StanowiskoViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path("stanowisko/<int:id>/members/", views.stanowisko_members, name="stanowisko_members"),
    path("person/<int:id>/update", views.person_update, name="person_update"),
    path("person/<int:id>/delete", views.person_delete, name="person_delete"),
    path('api/token/', obtain_auth_token, name='api_token_auth'),  
    path('api-auth/', include('rest_framework.urls')),  
    path('', include(router.urls)),  
    path("team/<int:id>", team_detail),  
    path("teams", team_list),  
    path("person/<int:id>", person_detail),  
    path("persons", person_list), 
    path("welcome", welcome_view),  
    path('admin/', admin.site.urls),  
]
