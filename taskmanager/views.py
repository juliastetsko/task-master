from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from taskmanager.models import Task


@login_required
def index(request):
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(is_completed=True).count()
    context = {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
    }
    return render(request, "taskmanager/index.html", context=context)
