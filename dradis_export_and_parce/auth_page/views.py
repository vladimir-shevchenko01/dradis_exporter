import requests
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import ExportForm

from auth_page.forms import ExportForm


def form_page(request):
    if request.method == 'POST':
        form = ExportForm(request.POST)
        if form.is_valid():
            # Authenticate with Dradis
            url = 'https://dradis.passpointsecurity.com/pro/login'
            data = {'username': 'email', 'password': 'password'}
            response = requests.post(url, data=data)
            auth_token = response.cookies.get('auth_token')
            if auth_token is not None:
                # Authenticate the user
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    # Login the user and redirect to the requested page
                    login(request, user)
                    return redirect('home')
                else:
                    form.add_error(None, "Invalid username or password")
            else:
                form.add_error(None, "Failed to authenticate with Dradis")
    else:
        form = ExportForm()
    context = {'form': form}
    return render(request, 'auth_page/login.html', context)


def login_view(request):
    user = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/')
        else:
            messages.error(request, 'Invalid username or password.')
    

def logout_view(request):
    logout(request)
    return redirect('login')
