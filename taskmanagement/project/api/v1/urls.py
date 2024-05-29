from django.urls import path

from project.api.v1.views import ProjectDetailView, ProjectView

urlpatterns = [
    path("", ProjectView.as_view(), name="collaborator"),
    path(
        "<int:project_id>/",
        ProjectDetailView.as_view(),
        name="collaborator details",
    ),
]

app_name = "project"
