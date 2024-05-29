from django.conf import settings
from django.db import models

from .constants import ROLE


class Collaborator(models.Model):
    class Meta:
        indexes = [
            models.Index(
                fields=("role", "description"),
                name="collab_role_description_idx",
            ),
        ]

    description = models.TextField(max_length=2000, null=True, blank=True)
    role = models.CharField(max_length=16, choices=ROLE, default=ROLE[0])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f"{self.role}-{self.id}"
