from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def Home(request):
    ptf = Portfolio.objects.first()
    return render(request, 'home.html', {'ptf': ptf})

def Skills(request):
    return render(request, 'skills.html')

def Projects(request):
    return render(request, 'projects.html')

def Experience(request):
    return render(request, 'experience.html')

def Others(request):
    return render(request, 'others.html')

def Contact(request):
    return render(request, 'contact.html')