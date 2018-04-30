from django.urls import path

from user.views import welcome

urlpatterns = [
    path('', welcome)
]
