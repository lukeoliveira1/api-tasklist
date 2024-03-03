from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ["id", "title", "status", "description", "status_display"]

    def get_status_display(self, obj):
        return obj.get_status_display()
