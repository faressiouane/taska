from django.shortcuts import render
from .models import List

def home(request):
    tasks = List.objects.all()
    return render(request, 'home.html', {'tasks' : tasks})