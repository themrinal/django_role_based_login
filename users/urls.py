# Import the path function to define URL routes
from django.urls import path

# Import the views from the current app (users)
from . import views

# This app namespace helps in uniquely identifying URLs from this app when using {% url %} in templates
app_name = "users"

# Define the list of URL patterns for the 'users' app
urlpatterns = [

    # The root path of the users app ('/user/') will show the login page
    path('', views.user_login, name='login'),

    # If the logged-in user is a counsellor, redirect to their dashboard
    path('counsellor_dashboard/', views.counsellor_dashboard, name='counsellor_dashboard'),

    # HOD dashboard path
    path('hod_dashboard/', views.hod_dashboard, name='hod_dashboard'),

    # Accountant dashboard path
    path('accountant_dashboard/', views.accountant_dashboard, name='accountant_dashboard'),

    # Principal dashboard path
    path('principal_dashboard/', views.principal_dashboard, name='principal_dashboard'),
]
