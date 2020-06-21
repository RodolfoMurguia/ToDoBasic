from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

from .models import  *
from .forms import *

#Creo mi primera vista dentro de la app

def index(request):
    #return HttpResponse('Bienvenido a la pestaña Tareas de la app To Do')
    tasks = Task.objects.all()

    form = CreateTask()

    if(request.method == 'POST'):
        form = CreateTask(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    TaskData = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', TaskData)

def editTask(request, pk):
    task = Task.objects.get(id = pk)

    form = CreateTask(instance=task)

    if(request.method == 'POST'):
        form = CreateTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    taskData = {'form':form}
    return render(request, 'tasks/editTask.html', taskData)

def deleteTask(request,pk):
    item = Task.objects.get(id = pk)

    if(request.method == 'POST'):
        item.delete()
        return redirect('/')

    taskData = {'item': item}
    return render(request, 'tasks/deleteTask.html', taskData)