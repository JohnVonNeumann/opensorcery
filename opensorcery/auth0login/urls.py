from django.urls import path, include


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]
