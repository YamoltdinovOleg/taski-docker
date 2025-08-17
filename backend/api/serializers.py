"""Serializers for Task model."""

from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for Task model."""

    class Meta:
        """Meta class for TaskSerializer."""

        model = Task
        fields = '__all__'


class TaskListSerializer(serializers.ModelSerializer):
    """Serializer for Task list view."""

    class Meta:
        """Meta class for TaskListSerializer."""

        model = Task
        fields = ['id', 'title', 'completed']
