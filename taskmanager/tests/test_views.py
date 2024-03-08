from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from taskmanager.models import Task, TaskType, Position

INDEX_URL = reverse("taskmanager:index")
TASK_LIST_URL = reverse("taskmanager:task-list")
WORKER_LIST_URL = reverse("taskmanager:worker-list")


class PublicViewTests(TestCase):
    def test_login_required(self) -> None:
        result_index = self.client.get(INDEX_URL)
        result_task = self.client.get(TASK_LIST_URL)
        worker_task = self.client.get(WORKER_LIST_URL)
        self.assertNotEqual(result_index.status_code, 200)
        self.assertNotEqual(result_task.status_code, 200)
        self.assertNotEqual(worker_task.status_code, 200)


class PrivateTaskViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="yulia",
            password="Test12345"
        )
        self.client.force_login(self.user)
        self.task = Task.objects.create(
            name="Fix bug",
            description="Fix bug on the project",
            deadline="2024-01-04",
            priority="high",
            task_type=TaskType.objects.create(name="Bug"),
            created_at="2024-20-03",
        )
        self.task.assignees.set(get_user_model().objects.all())

    def test_retrieve_task_list(self) -> None:
        response = self.client.get(TASK_LIST_URL)
        self.assertEqual(response.status_code, 200)
        tasks = Task.objects.all()
        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks),
        )
        self.assertTemplateUsed(response, "taskmanager/task_list.html")


class PrivateWorkerViewTest(TestCase):
    def setUp(self):
        self.position = Position.objects.create(name="Developer")
        self.user = get_user_model().objects.create_user(
            username="yulia",
            password="Test12345",
            first_name="Yuliia",
            last_name="Stetsko",
            position=self.position,
        )
        self.client.force_login(self.user)

    def test_retrieve_worker_list(self) -> None:
        response = self.client.get(WORKER_LIST_URL)
        self.assertEqual(response.status_code, 200)
        workers = get_user_model().objects.all()
        self.assertEqual(
            list(response.context["worker_list"]),
            list(workers),
        )
        self.assertTemplateUsed(response, "taskmanager/worker_list.html")
