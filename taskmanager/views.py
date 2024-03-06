from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

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


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
