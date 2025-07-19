from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def userhome(req):
    return HttpResponse("Hello User!")