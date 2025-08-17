"""Views for Task API."""

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Task
from .serializers import TaskListSerializer, TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """ViewSet for Task model."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request):
        """List all tasks with simplified serializer."""
        queryset = self.get_queryset()
        serializer = TaskListSerializer(queryset, many=True)
        return Response(serializer.data)
