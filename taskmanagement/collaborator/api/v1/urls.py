from django.urls import path

from collaborator.api.v1.views import CollaboratorDetailView, CollaboratorView

urlpatterns = [
    path("", CollaboratorView.as_view(), name="collaborator"),
    path(
        "<int:collaborator_id>/",
        CollaboratorDetailView.as_view(),
        name="collaborator details",
    ),
]

app_name = "collaborator"
