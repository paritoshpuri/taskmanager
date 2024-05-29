from rest_framework import status

from task.api.v1.serializers import TaskSerializer
from task.models import Task, TaskLogs
from taskmanagement.utils import BaseService


class TaskService(BaseService):

    def get_task(self, request, kwargs):
        task = Task.objects.all()
        view_serializer = TaskSerializer(data=task, many=True)
        view_serializer.is_valid()
        return self.set_response(data=view_serializer.data)

    def add_task(self, request):
        create_serializer = TaskSerializer(
            data=request.data, context={"request": request}
        )
        if not create_serializer.is_valid():
            self.set_response(
                code=status.HTTP_400_BAD_REQUEST,
                errors=create_serializer.errors,
                message=f"Invalid task details payload",
            )
            return self.response
        create_serializer.save()
        return self.set_response(code=status.HTTP_201_CREATED)


class TaskDetailService(BaseService):

    def get_task_by_id(self, request, kwargs):
        task_id = kwargs.get("task_id")
        task = Task.objects.filter(id=task_id)
        if not task:
            return self.set_response(
                code=status.HTTP_400_BAD_REQUEST,
                errors=f"object not found for id {task_id}",
                message="please provide valid id",
            )
        view_serializer = TaskSerializer(data=task, many=True)
        view_serializer.is_valid()
        return self.set_response(data=view_serializer.data)

    def delete_task(self, request, kwargs):
        task_id = kwargs.get("task_id")
        task = Task.objects.filter(id=task_id)
        if task:
            task.delete()
            return self.set_response(code=status.HTTP_204_NO_CONTENT)
        return self.set_response(
            code=status.HTTP_400_BAD_REQUEST, errors="id not found"
        )

    def update_task(self, request, kwargs):
        create_serializer = TaskSerializer(
            data=request.data, context={"request": request}
        )
        if not create_serializer.is_valid():
            return self.set_response(
                code=status.HTTP_400_BAD_REQUEST,
                errors=create_serializer.errors,
                message=f"Invalid task details payload",
            )
        task_id = kwargs.get("task_id")
        task = Task.objects.filter(id=task_id)
        if task:
            task.update(**create_serializer.validated_data)
            log_data = {"task": task.first(), "changed_by": request.user}
            TaskLogs.objects.create(**log_data)
            return self.set_response()
        return self.set_response(
            code=status.HTTP_400_BAD_REQUEST,
            errors="id not found",
            message="need valid id",
        )
