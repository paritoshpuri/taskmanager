from rest_framework import status

from project.api.v1.serializers import ProjectSerializer
from project.models import Project
from taskmanagement.utils import BaseService


class ProjectService(BaseService):

    def get_project(self, request, kwargs):
        project = Project.objects.all()
        view_serializer = ProjectSerializer(data=project, many=True)
        view_serializer.is_valid()
        return self.set_response(data=view_serializer.data)

    def add_project(self, request):
        create_serializer = ProjectSerializer(
            data=request.data, context={"request": request}
        )
        if not create_serializer.is_valid():
            self.set_response(
                code=status.HTTP_400_BAD_REQUEST,
                errors=create_serializer.errors,
                message=f"Invalid project details payload",
            )
            return self.response
        create_serializer.save()
        return self.set_response(code=status.HTTP_201_CREATED)


class ProjectDetailService(BaseService):

    def get_project_by_id(self, request, kwargs):
        project_id = kwargs.get("project_id")
        project = Project.objects.filter(id=project_id)
        if not project:
            return self.set_response(
                code=status.HTTP_400_BAD_REQUEST,
                errors=f"object not found for id {project_id}",
                message="please provide valid id",
            )
        view_serializer = ProjectSerializer(data=project, many=True)
        view_serializer.is_valid()
        return self.set_response(data=view_serializer.data)

    def delete_project(self, request, kwargs):
        project_id = kwargs.get("project_id")
        project = Project.objects.filter(id=project_id)
        if project:
            project.delete()
            return self.set_response(code=status.HTTP_204_NO_CONTENT)
        return self.set_response(
            code=status.HTTP_400_BAD_REQUEST, errors="id not found"
        )

    def update_project(self, request, kwargs):
        create_serializer = ProjectSerializer(
            data=request.data, context={"request": request}
        )
        if not create_serializer.is_valid():
            return self.set_response(
                code=status.HTTP_400_BAD_REQUEST,
                errors=create_serializer.errors,
                message=f"Invalid project details payload",
            )
        project_id = kwargs.get("project_id")
        project = Project.objects.filter(id=project_id)
        if project:

            project.update(**create_serializer.validated_data)
            return self.set_response()
        return self.set_response(
            code=status.HTTP_400_BAD_REQUEST,
            errors="id not found",
            message="need valid id",
        )
