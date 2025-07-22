from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.user_login, name='login'),
    path('counsellor_dashboard/', views.counsellor_dashboard, name='counsellor_dashboard'),
    path('hod_dashboard/', views.hod_dashboard, name='hod_dashboard'),
    path('accountant_dashboard/', views.accountant_dashboard, name='accountant_dashboard'),
    path('principal_dashboard/', views.principal_dashboard, name='principal_dashboard'),
]
