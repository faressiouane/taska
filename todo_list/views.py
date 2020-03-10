from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task has been added to the list')
        return redirect('home')

    else:
        tasks = List.objects.all()
        return render(request, 'home.html', {'tasks' : tasks,})