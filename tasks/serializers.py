from rest_framework import serializers

from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status_display")
    
    class Meta:
        model = Task
        fields = ["id", "title", "status", "description"]