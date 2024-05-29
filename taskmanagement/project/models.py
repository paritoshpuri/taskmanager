from django.conf import settings
from django.db import models


class Project(models.Model):
    class Meta:
        indexes = [
            models.Index(
                fields=("name", "url"),
                name="projects_name_url_idx",
            ),
        ]

    name = models.CharField(max_length=32)
    url = models.URLField(blank=True, null=True)
    description = models.TextField(max_length=2048, null=True, blank=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="projects_created",
        on_delete=models.SET_NULL,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)
