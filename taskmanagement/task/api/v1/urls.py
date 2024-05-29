from django.urls import path

from task.api.v1.views import TaskDetailView, TaskView

urlpatterns = [
    path("", TaskView.as_view(), name="collaborator"),
    path(
        "<int:task_id>/",
        TaskDetailView.as_view(),
        name="collaborator details",
    ),
]

app_name = "task"
