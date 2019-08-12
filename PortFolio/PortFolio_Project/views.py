from django.shortcuts import render
from .models import Project
# Create your views here.

def HomePage(request):
    projects = Project.objects.all()
    context = {
    'projects':projects,
    }
    return render(request, 'PortFolio_Project/HomePage.html', context)

def Details(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
    'project':project,
    }
    return render(request, 'PortFolio_Project/Details.html', context)
