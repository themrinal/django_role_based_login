# Import functions to render HTML templates, handle redirects, and authenticate users
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

# Import the login form from forms.py
from .forms import LoginForm

# Import custom decorator that restricts access to specific roles
from .decorators import role_required


# USER LOGIN VIEW
# ---------------------------
def user_login(request):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Bind submitted data to the form
        form = LoginForm(request.POST)
        
        # Validate the form
        if form.is_valid():
            # Extract username and password from the cleaned form data
            uname = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            
            # Authenticate the user using Django's built-in function
            user = authenticate(request, username=uname, password=pwd)
            
            # If user credentials are valid
            if user:
                # Log the user in (starts a session)
                login(request, user)

                # Get the user's role from their profile
                role = user.userprofile.role

                # Redirect user to their role-based dashboard
                return redirect(f'/user/{role}_dashboard/')
            else:
                # Invalid login credentials
                return HttpResponse("Invalid credentials")
    else:
        # If the request is GET, display a fresh login form
        form = LoginForm()
    
    # Render the login template with the form
    return render(request, 'users/login.html', {'form': form})



# ROLE-SPECIFIC DASHBOARDS
# ---------------------------

# Only users with the 'counsellor' role can access this view
@role_required(['counsellor'])
def counsellor_dashboard(request):
    return render(request, 'users/counsellor_dashboard.html')


# Only users with the 'hod' role can access this view
@role_required(['hod'])
def hod_dashboard(request):
    return render(request, 'users/hod_dashboard.html')


# Only users with the 'accountant' role can access this view
@role_required(['accountant'])
def accountant_dashboard(request):
    return render(request, 'users/accountant_dashboard.html')


# Only users with the 'principal' role can access this view
@role_required(['principal'])
def principal_dashboard(request):
    return render(request, 'users/principal_dashboard.html')
