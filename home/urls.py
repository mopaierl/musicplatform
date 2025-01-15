from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Importiere eigene Views, falls du sie brauchst

urlpatterns = [
    path('', views.home, name="home"),
]