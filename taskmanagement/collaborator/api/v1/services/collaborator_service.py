from rest_framework import status

from collaborator.api.v1.serializers import CollaboratorSerializer
from collaborator.models import Collaborator
from taskmanagement.utils import BaseService


class CollaboratorService(BaseService):

    def get_collaborator(self, request, kwargs):
        collaborator = Collaborator.objects.all()
        view_serializer = CollaboratorSerializer(data=collaborator, many=True)
        view_serializer.is_valid()
        return self.set_response(data=view_serializer.data)

    def add_collaborator(self, request):
        create_serializer = CollaboratorSerializer(
            data=request.data, context={"request": request}
        )
        if not create_serializer.is_valid():
            self.set_response(
                code=status.HTTP_400_BAD_REQUEST,
                errors=create_serializer.errors,
                message=f"Invalid Collaborator details payload",
            )
            return self.response
        create_serializer.save()
        return self.set_response(code=status.HTTP_201_CREATED)


class CollaboratorDetailService(BaseService):

    def get_collaborator_by_id(self, request, kwargs):
        collaborator_id = kwargs.get("collaborator_id")
        collaborator = Collaborator.objects.filter(id=collaborator_id)
        if not collaborator:
            return self.set_response(
                code=status.HTTP_400_BAD_REQUEST,
                errors=f"object not found for id {collaborator_id}",
                message="please provide valid id",
            )
        view_serializer = CollaboratorSerializer(data=collaborator, many=True)
        view_serializer.is_valid()
        return self.set_response(data=view_serializer.data)

    def delete_collaborator(self, request, kwargs):
        collaborator_id = kwargs.get("collaborator_id")
        collaborator = Collaborator.objects.filter(id=collaborator_id)
        if collaborator:
            collaborator.delete()
            return self.set_response(code=status.HTTP_204_NO_CONTENT)
        return self.set_response(
            code=status.HTTP_400_BAD_REQUEST, errors="id not found"
        )

    def update_collaborator(self, request, kwargs):
        create_serializer = CollaboratorSerializer(
            data=request.data, context={"request": request}
        )
        if not create_serializer.is_valid():
            return self.set_response(
                code=status.HTTP_400_BAD_REQUEST,
                errors=create_serializer.errors,
                message=f"Invalid Collaborator details payload",
            )
        collaborator_id = kwargs.get("collaborator_id")
        collaborator = Collaborator.objects.filter(id=collaborator_id)
        if collaborator:

            collaborator.update(**create_serializer.validated_data)
            return self.set_response()
        return self.set_response(
            code=status.HTTP_400_BAD_REQUEST,
            errors="id not found",
            message="need valid id",
        )
