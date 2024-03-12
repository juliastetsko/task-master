from django.contrib.auth import get_user_model
from django.test import TestCase

from taskmanager.models import Task, TaskType, Position


class ModelsTest(TestCase):

    def setUp(self) -> None:
        self.task_type = TaskType.objects.create(name="Bug")
        self.position = Position.objects.create(name="Developer")
        self.worker = get_user_model().objects.create_user(
            username="yulia",
            password="Test12345",
            first_name="Yuliia",
            last_name="Stetsko",
            position=self.position,
        )

        self.task = Task.objects.create(
            name="Fix bug",
            description="Fix bug on the project",
            deadline="2024-01-04",
            priority=Task.Priorities.HIGH,
            task_type=self.task_type,
            created_at="2024-20-03",
        )
        self.task.assignees.set(get_user_model().objects.all())

    def test_task_type_str(self) -> None:
        task_type = self.task_type
        self.assertEqual(str(task_type), task_type.name)

    def test_worker_str(self) -> None:
        worker = self.worker
        self.assertEqual(
            str(worker),
            f"{worker.username} ({worker.first_name} {worker.last_name} {worker.position})"
        )

    def test_position_str(self) -> None:
        position = self.position
        self.assertEqual(str(position), position.name)
