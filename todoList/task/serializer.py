from .models import Task
from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Task
    fields = ('user', 'name', 'created_date')

