from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.exceptions import ValidationError
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()  # <-- Explicitly define queryset here
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter tasks by the logged-in user
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Assign the task to the logged-in user
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        # Prevent completed tasks from being updated
        task = self.get_object()
        if task.status == 'Completed':
            raise ValidationError('Cannot modify a completed task')
        serializer.save()

    def perform_destroy(self, instance):
        # Prevent completed tasks from being deleted
        if instance.status == 'Completed':
            raise ValidationError('Cannot delete a completed task')
        instance.delete()
