from django.shortcuts import render
from .models import Portfolio
from .models import Skill
# Create your views here.
def Home(request):
    ptf = Portfolio.objects.first()
    return render(request, 'home.html', {'ptf': ptf})

def Skills(request):
    skills = Skill.objects.all()
    return render(request, 'skills.html', {'skills': skills})

def Projects(request):
    return render(request, 'projects.html')

def Experience(request):
    return render(request, 'experience.html')

def Others(request):
    return render(request, 'others.html')

def Contact(request):
    return render(request, 'contact.html')