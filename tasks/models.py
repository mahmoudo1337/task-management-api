from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    PRIORITY_CHOICES = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]

    PENDING = 'Pending'
    COMPLETED = 'Completed'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default=MEDIUM)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
