from django.shortcuts import render
from .models import Portfolio
from .models import Skill
# Create your views here.
def Home(request):
    ptf = Portfolio.objects.first()
    skills = ptf.skills.all()
    return render(request, 'base.html', {'ptf': ptf, 'skills': skills})


def Contact(request):
    return render(request, 'contact.html')