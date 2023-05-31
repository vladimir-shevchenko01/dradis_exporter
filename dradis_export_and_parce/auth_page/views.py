from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from auth_page.forms import ExportForm


def form_page(request):
    form = ExportForm(
        request.POST or None,)
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
