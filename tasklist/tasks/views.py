from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect, HttpResponse
# Create your views here.
from .forms import TaskForm
from datetime import datetime

from django.views.generic.detail import DetailView
from .models import Task

def task_new(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.created_on = datetime.now()
            task.amended_by = request.user
            task.amended_on = datetime.now()
            task.save()
            return redirect('/tasks/', request)
                                        # {'task_list': Task.objects.all() } )
    else:
        form = TaskForm()

        return render(request, 'tasks/task_edit.html', {'form': form})

def task_list(request):
    return render_to_response('tasks/task_index.html',
                                {'task_list': Task.objects.all(), 'request':request } )

def task_detail(pk):
    return redirect('tasks/thanks.html')
