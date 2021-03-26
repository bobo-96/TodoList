from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from categories.models import Category
from categories.permissions import IsCategoryOwnerOrReadOnly
from categories.serializers import CategorySerializer


class CategoryView(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'
    permission_classes = (IsCategoryOwnerOrReadOnly,)
