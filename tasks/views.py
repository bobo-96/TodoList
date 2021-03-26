from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from tasks.models import Task
from tasks.permissions import IsTaskOwnerOrReadOnly
from tasks.serializers import TaskSerializer


class TaskView(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'pk'
    permission_classes = (IsTaskOwnerOrReadOnly,)