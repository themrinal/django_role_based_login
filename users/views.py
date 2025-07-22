from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import LoginForm
from .decorators import role_required

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(request, username=uname, password=pwd)
            if user:
                login(request, user)
                role = user.userprofile.role
                return redirect(f'/user/{role}_dashboard/')
            else:
                return HttpResponse("Invalid credentials")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

@role_required(['counsellor'])
def counsellor_dashboard(request):
    return render(request, 'users/counsellor_dashboard.html')

@role_required(['hod'])
def hod_dashboard(request):
    return render(request, 'users/hod_dashboard.html')

@role_required(['accountant'])
def accountant_dashboard(request):
    return render(request, 'users/accountant_dashboard.html')

@role_required(['principal'])
def principal_dashboard(request):
    return render(request, 'users/principal_dashboard.html')
