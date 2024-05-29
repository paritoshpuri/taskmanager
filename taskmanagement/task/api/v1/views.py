from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from task.api.v1.services.task_service import TaskDetailService, TaskService


class TaskView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        response = TaskService().get_task(request, kwargs)
        return Response(response, status=response.get("code"))

    def post(self, request, *args, **kwargs):
        response = TaskService().add_task(request)
        return Response(response, status=response.get("code"))


class TaskDetailView(APIView):

    def get(self, request, *args, **kwargs):
        response = TaskDetailService().get_task_by_id(request, kwargs)
        return Response(response, status=response.get("code"))

    def delete(self, request, *args, **kwargs):
        response = TaskDetailService().delete_task(request, kwargs)
        return Response(response, status=response.get("code"))

    def put(self, request, *args, **kwargs):
        response = TaskDetailService().update_task(request, kwargs)
        return Response(response, status=response.get("code"))
