from django.shortcuts import render
from .models import *


# Create your views here.
def history(request):
    exam = History.objects.all()
    return render(request, "index.html", {"exam": exam})

def geography(request):
    exam = Geography.objects.all()
    return render(request, "index.html", {"exam": exam})

def science(request):
    exam = Science.objects.all()
    return render(request, "index.html", {"exam": exam})
