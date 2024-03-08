from django import forms
from django.contrib.auth import get_user_model
from django.test import TestCase

from taskmanager.forms import TaskSearchForm, TaskForm


class TestTaskSearchForm(TestCase):
    def test_task_name_search_form(self) -> None:
        form = TaskSearchForm(
            data={"name": "fix big"}
        )
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "fix big")

    def test_task_assignee_search_form(self) -> None:
        form = TaskSearchForm(
            data={"assignee": "yulia"}
        )
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["assignee"], "yulia")

    def test_task_include_completed_search_form(self) -> None:
        form = TaskSearchForm(
            data={"include_completed": True}
        )
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["include_completed"], True)


class TaskFormTest(TestCase):
    def test_assignees_field(self):
        get_user_model().objects.create(username="yulia")
        get_user_model().objects.create(username="alisa")
        form = TaskForm()
        self.assertTrue(isinstance(form.fields["assignees"], forms.ModelMultipleChoiceField))
        self.assertFalse(form.fields["assignees"].required)
