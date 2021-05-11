from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def user_authentication(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, 'invalid username or password')
    return render(request, 'user.html', {})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {})



def logout(request):
    auth.logout(request)
    return redirect('/')