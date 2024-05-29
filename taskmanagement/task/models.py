from django.conf import settings
from django.db import models

from collaborator.models import Collaborator
from project.models import Project


class Task(models.Model):
    class Meta:
        indexes = [
            models.Index(
                fields=("state", "-priority", "-deadline"),
                name="tasks_task_priority_idx",
            ),
        ]

    STATES = (
        ("To Do", "To Do"),
        ("In Progress", "In Progress"),
        ("Blocked", "Blocked"),
        ("Done", "Done"),
        ("Abandoned", "Abandoned"),
    )

    PRIORITIES = (
        ("Low", "Low"),
        ("Normal", "Normal"),
        ("High", "High"),
    )

    title = models.CharField(max_length=128)
    project = models.ForeignKey(
        Project, blank=True, null=True, on_delete=models.CASCADE
    )
    collaborator = models.ManyToManyField(Collaborator, blank=True)
    description = models.TextField(max_length=1024, null=True, blank=True)
    resolution = models.TextField(max_length=1024, null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="tasks_assigned",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    state = models.CharField(max_length=16, choices=STATES, default=STATES[0])
    priority = models.CharField(
        max_length=16, choices=PRIORITIES, default=PRIORITIES[0]
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="users_created",
        on_delete=models.SET_NULL,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.title}-{self.state}"

    def get_collaborator(self):
        return ",".join([str(p) for p in self.collaborator.all()])


class TaskLogs(models.Model):
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    changed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    last_modified = models.DateTimeField(auto_now=True, editable=False)
