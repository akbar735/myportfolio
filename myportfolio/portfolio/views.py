from django.shortcuts import render
from .models import Portfolio
from .models import Skill
# Create your views here.
def Home(request):
    ptf = Portfolio.objects.first()
    return render(request, 'home.html', {'ptf': ptf})

def Skills(request):
    portfolio = Portfolio.objects.get(id=1)
    skills = portfolio.skills.all()
    return render(request, 'skills.html', {'skills': skills})

def Projects(request):
    portfolio = Portfolio.objects.get(id=1)
    projects = portfolio.projects.prefetch_related('techstack').all()

    return render(request, 'projects.html', {'projects': projects})

def Experience(request):
    return render(request, 'experience.html')

def Others(request):
    return render(request, 'others.html')

def Contact(request):
    return render(request, 'contact.html')