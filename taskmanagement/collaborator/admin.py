from django.contrib import admin

from .models import Collaborator


# Register your models here.
@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ("user", "description", "role", "created_at", "last_modified")
    list_display_links = ("user",)
    search_fields = ("user", "role")
