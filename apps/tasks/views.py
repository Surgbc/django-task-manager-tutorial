from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .forms import TaskForm


@login_required
def task_list(request):
    tasks = Task.objects.filter(assigned_to=request.user)
    context = {'tasks': tasks}
    return render(request, 'tasks/task_list.html', context)


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk, assigned_to=request.user)
    context = {'task': task}
    return render(request, 'tasks/task_detail.html', context)


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_to = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()
    
    context = {'form': form, 'title': 'Create Task'}
    return render(request, 'tasks/task_form.html', context)


@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, assigned_to=request.user)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_detail', pk=task.pk)
    else:
        form = TaskForm(instance=task)
    
    context = {'form': form, 'task': task, 'title': 'Update Task'}
    return render(request, 'tasks/task_form.html', context)


@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, assigned_to=request.user)
    
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')
    
    context = {'task': task}
    return render(request, 'tasks/task_confirm_delete.html', context)