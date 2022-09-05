from rest_framework import serializers

from task.models import Task, Subtask


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ["id", "subtask_name", "done"]


class TaskSerializer(serializers.ModelSerializer):
    subtask = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field="subtask_name"
    )

    class Meta:
        model = Task
        fields = ["id", "task_name", "done", "created_at", "subtask", "user"]
        read_only_fields = ("user",)
