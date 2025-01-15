from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Importiere eigene Views, falls du sie brauchst
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.profile, name="profile"),
    path('register/', views.register_view, name="register"),
    path('login/',views.login_view, name="login"),
    path('logout/', LogoutView.as_view(next_page='/profile/login/'), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

]