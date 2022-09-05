from django.db import models
from rest_framework.authtoken.admin import User


class Subtask(models.Model):
    subtask_name = models.TextField()
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.subtask_name


class Task(models.Model):
    task_name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_tasks"
    )
    subtask = models.OneToOneField(
        Subtask,
        on_delete=models.CASCADE,
        blank=True
    )

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return self.task_name
