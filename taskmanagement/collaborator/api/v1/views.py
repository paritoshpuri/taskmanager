from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from collaborator.api.v1.services.collaborator_service import (
    CollaboratorDetailService, CollaboratorService)


class CollaboratorView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        response = CollaboratorService().get_collaborator(request, kwargs)
        return Response(response, status=response.get("code"))

    def post(self, request, *args, **kwargs):
        response = CollaboratorService().add_collaborator(request)
        return Response(response, status=response.get("code"))


class CollaboratorDetailView(APIView):

    def get(self, request, *args, **kwargs):
        response = CollaboratorDetailService().get_collaborator_by_id(request, kwargs)
        return Response(response, status=response.get("code"))

    def delete(self, request, *args, **kwargs):
        response = CollaboratorDetailService().delete_collaborator(request, kwargs)
        return Response(response, status=response.get("code"))

    def put(self, request, *args, **kwargs):
        response = CollaboratorDetailService().update_collaborator(request, kwargs)
        return Response(response, status=response.get("code"))
