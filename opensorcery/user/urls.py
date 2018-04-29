from django.urls import path

from user.views import login, welcome

urlpatterns = [
    path('', login),
    path('welcome', welcome)
]
