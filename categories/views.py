from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from categories.models import Category
from categories.permissions import IsCategoryOwnerOrReadOnly
from categories.serializers import CategorySerializer


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.prefetch_related('owner')
    lookup_field = 'pk'
    permission_classes = (IsCategoryOwnerOrReadOnly,)

    def list(self, request, *args, **kwargs):
        user = request.user
        queryset = Category.objects.filter(owner=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
