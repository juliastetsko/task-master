from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taskmanager.models import TaskType, Position, Worker, Task


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                    )
                },
            ),
        )
    )


admin.site.register(Task)
admin.site.register(TaskType)
admin.site.register(Position)
