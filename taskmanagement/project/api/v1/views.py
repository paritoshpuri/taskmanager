from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from project.api.v1.services.project_service import (ProjectDetailService,
                                                     ProjectService)


class ProjectView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        response = ProjectService().get_project(request, kwargs)
        return Response(response, status=response.get("code"))

    def post(self, request, *args, **kwargs):
        response = ProjectService().add_project(request)
        return Response(response, status=response.get("code"))


class ProjectDetailView(APIView):

    def get(self, request, *args, **kwargs):
        response = ProjectDetailService().get_project_by_id(request, kwargs)
        return Response(response, status=response.get("code"))

    def delete(self, request, *args, **kwargs):
        response = ProjectDetailService().delete_project(request, kwargs)
        return Response(response, status=response.get("code"))

    def put(self, request, *args, **kwargs):
        response = ProjectDetailService().update_project(request, kwargs)
        return Response(response, status=response.get("code"))
