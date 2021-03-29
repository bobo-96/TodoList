from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from tasks.models import Task
from tasks.permissions import IsTaskOwnerOrReadOnly
from tasks.serializers import TaskSerializer
from user.models import User


class TaskView(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.prefetch_related('category')
    lookup_field = 'pk'
    permission_classes = (IsTaskOwnerOrReadOnly,)

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = Task.objects.filter(owner=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


