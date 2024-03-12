from django import forms
from django.contrib.auth import get_user_model

from taskmanager.models import Task


class TaskSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )
    assignee = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by assignee"
            }
        )
    )
    include_completed = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'onclick': 'this.form.submit();'}),
        label="Include completed"
    )


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local"}
        )
    )
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


    class Meta:
        model = Task
        fields = "__all__"
