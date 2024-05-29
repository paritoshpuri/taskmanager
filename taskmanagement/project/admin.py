from django.contrib import admin

from .models import Project


# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "url",
        "description",
        "created_by",
        "created_at",
        "last_modified",
    )
    list_display_links = ("url", "created_by")
    search_fields = ("created_by", "name")
