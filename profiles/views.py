from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate





def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())

def editData(request):
    template = loader.get_template('editData.html')
    return HttpResponse(template.render())


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Erfolgreich eingeloggt!")
            return redirect('home')  # Redirect zur Startseite oder einer anderen Seite
        else:
            messages.error(request, "Ungültige Anmeldedaten.")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Benutzer wird gespeichert
            messages.success(request, "Dein Account wurde erfolgreich erstellt!")
            return redirect('login')  # Weiterleitung zur Login-Seite
        else:
            messages.error(request, "Fehler bei der Registrierung.")
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/register.html', {'form': form})

# views.py
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

def logout_view(request):
    auth_logout(request)
    return redirect('login')  # Weiterleitung zur Login-Seite nach dem Logout

