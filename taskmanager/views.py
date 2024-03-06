from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from taskmanager.forms import TaskNameSearchForm
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
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = TaskNameSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Task.objects.all()
        form = TaskNameSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
