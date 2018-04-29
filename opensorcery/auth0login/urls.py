from django.urls import path, include

from auth0login.views import index, dashboard

urlpatterns = [
    path('', index),
    path('dashboard', dashboard),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]
