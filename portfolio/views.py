from django.shortcuts import render
from django.http import HttpRequest
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request,'portfolio/home.html',{'Projects':projects})
