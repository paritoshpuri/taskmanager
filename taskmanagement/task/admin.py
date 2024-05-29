from django.contrib import admin

from .models import Task, TaskLogs


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "project",
        "description",
        "owner",
        "deadline",
        "priority",
        "state",
        "resolution",
        "get_collaborator",
    )
    list_display_links = ("project", "owner")
    search_fields = ("deadline", "priority", "state")


@admin.register(TaskLogs)
class TaskLogsAdmin(admin.ModelAdmin):
    list_display = ("task", "changed_by")
    list_display_links = ("task",)
    search_fields = ("task",)
