from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .forms import TaskForm
from django.contrib import messages
# para exibir mensagens 
 

from .models import Task


# Create your views here.

def taskList(request):
    tasks = Task.objects.all().order_by('-created_at')
    return render(request,'tasks/index.html', {'tasks':tasks})  

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('/')
            # preciso revisar essa parte depois 
    else:
        form = TaskForm()
        return render(request, 'tasks/novo.html', {'form': form})

def deleteTask(request, id):
    task = get_object_or_404 (Task, pk=id)   
    task.delete()
    messages.info(request, 'Empresa Deletada!')
    return redirect('/')  

def helloword(request):
    return HttpResponse('primeira pagina django\o/')


  