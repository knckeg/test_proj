from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views 

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api/token/', views.obtain_auth_token, name='api_token_auth'), 
    path('', include('myapp.urls')), 
]

