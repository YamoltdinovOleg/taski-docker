"""Task model definition."""

from django.db import models


class Task(models.Model):
    """Task model for storing task information."""

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of the task."""
        return self.title
