from django.shortcuts import render, redirect, get_object_or_404
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

def delete(request, id):
    # item = List.objects.get(id = id)
    item = get_object_or_404(List, pk=id)
    item.delete()
    messages.success(request, 'Task has been deleted from the list')

    return redirect('home')

def reverse(request, id):
    item = get_object_or_404(List, pk=id)

    #reversing the bool value
    item.completed = not item.completed
    item.save()

    note = 'Crossed' if item.completed == True else "Un Crossed"
    messages.success(request, f'Task has been {note}')

    return redirect('home')

def edit(request, id):
    if request.method == "POST":
        item = get_object_or_404(List, pk = id)
        form = ListForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, 'Task has been updated !')
        else:
            messages.success(request, 'could not update ypur task') 

        return redirect('home')

    else:
        item = get_object_or_404(List, pk = id)
        return render(request, 'edit.html', {'task' : item})
